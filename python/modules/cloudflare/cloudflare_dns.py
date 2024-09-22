import configparser
import dns.resolver
import dns.rdatatype
import requests
import sys

# Load config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get Cloudflare API settings from config.ini
api_token = config['CLOUDFLARE']['api_token']

if api_token == " ":
    print("[ERROR] Failed to get token, open the config file and manualy enter it! (python\modules\cloudflare\config.ini)")

# Cloudflare API endpoint to retrieve all zones
api_endpoint = 'https://api.cloudflare.com/client/v4/zones'

# Set headers for Cloudflare API request
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

timeout = int(config['DNS']['timeout'])

# Get DNS resolver settings from config.ini
resolver = dns.resolver.Resolver()
resolver.timeout = timeout
resolver.nameservers = [config['DNS']['nameserver']]

# Make request to Cloudflare API
response = requests.get(api_endpoint, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Get list of zones from Cloudflare API response
    zones = response.json()['result']

    # Loop through zones and print details
    for zone in zones:
        domain = zone['name']
        zone_id = zone['id']

        print(f'\n--')
        print(f'Zone for {domain} (zone_id: {zone_id})')
        print(f'--')

        # Cloudflare API endpoint to retrieve DNS records for zone
        dns_api_endpoint = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type=A'

        # Make request to Cloudflare API to retrieve A records for zone
        dns_response = requests.get(dns_api_endpoint, headers=headers)

        # Check if request was successful
        if dns_response.status_code == 200:
            # Get list of A records from Cloudflare API response
            a_records = dns_response.json()['result']


            for a_record in a_records:
                name = a_record['name']
                value = a_record['content']
                ttl = a_record['ttl']

                try:
                    a_answer = resolver.resolve(
                        name, rdtype=dns.rdatatype.A)
                    ip = str(a_answer[0])
                    print(f'- IPv4 address for {name}: {ip}')
                except:
                    print('\033[91m- Error: DNS lookup failed\033[0m')
                    sys.exit(1)  # exit with error code

                
                try:
                    aaaa_answer = resolver.resolve(
                        name, rdtype=dns.rdatatype.AAAA)
                    ip = str(aaaa_answer[0])
                    print(f'- IPv6 address for {name}: {ip}')
                except:
                    print('\033[91m- Error: DNS lookup failed\033[0m')
                    sys.exit(1)  # exit with error code

               # Test HTTP endpoint
                try:
                    http_response = requests.get(
                        f'http://{name}/', timeout=timeout)
                    http_status = http_response.status_code
                    print(f'- HTTP status code for {name}: {http_status}')
                except:
                    print(
                        '\033[91m- Error: HTTP endpoint not reachable\033[0m')
                    http_status = None

                
                try:
                    https_response = requests.get(
                        f'https://{name}/', timeout=timeout)
                    https_status = https_response.status_code
                    print(
                        f'- HTTPS status code for {name}: {https_status}')
                except:
                    print(
                        '\033[91m- Error: HTTPS endpoint not reachable\033[0m')
                    https_status = None

                if http_status == None or https_status == None:
                    sys.exit(1)

sys.exit(0)