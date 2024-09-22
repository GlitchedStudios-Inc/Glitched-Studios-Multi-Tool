try:
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import re
    import urllib.parse
except Exception as e:
    print(f"Error: {e}")

def download_assets(website_url, base_url, output_dir):
    soup = BeautifulSoup(requests.get(website_url).content, 'html.parser')

    # Download HTML files
    html_links = soup.find_all('a', href=True)
    for link in html_links:
        html_url = link.get('href')
        if html_url:
            if html_url.startswith('/'):
                html_url = urljoin(base_url, html_url)
            elif html_url.startswith('https://') or html_url.startswith('http://'):
                pass
            else:
                continue

            response = requests.get(html_url)
            if response.status_code == 200:
                html_ext = os.path.splitext(html_url)[1][1:]  # Get the file extension
                if html_ext in ['html', 'htm', 'php']:  # Added 'php' to the list
                    with open(os.path.join(output_dir, os.path.basename(html_url)), 'w', encoding='utf-8') as file:
                        file.write(response.text)

    # Download CSS files
    css_links = soup.find_all('link', rel='stylesheet')
    for link in css_links:
        css_url = link.get('href')
        if css_url:
            if css_url.startswith('/'):
                css_url = urljoin(base_url, css_url)
            elif css_url.startswith('https://') or css_url.startswith('http://'):
                pass
            else:
                continue

            response = requests.get(css_url)
            if response.status_code == 200:
                css_ext = os.path.splitext(css_url)[1][1:]  # Get the file extension
                if css_ext in ['css']:
                    with open(os.path.join(output_dir, 'css', os.path.basename(css_url)), 'w', encoding='utf-8') as file:
                        file.write(response.text)

    # Download JavaScript files
    js_links = soup.find_all('script', src=True)
    for script in js_links:
        js_url = script.get('src')
        if js_url:
            if js_url.startswith('/'):
                js_url = urljoin(base_url, js_url)
            elif js_url.startswith('https://') or js_url.startswith('http://'):
                pass
            else:
                continue

            response = requests.get(js_url)
            if response.status_code == 200:
                js_ext = os.path.splitext(js_url)[1][1:]  # Get the file extension
                if js_ext in ['js']:
                    with open(os.path.join(output_dir, 'js', os.path.basename(js_url)), 'w', encoding='utf-8') as file:
                        file.write(response.text)

    # Download images
    img_links = soup.find_all('img')
    for img in img_links:
        img_url = img.get('src')
        if img_url:
            if img_url.startswith('/'):
                img_url = urljoin(base_url, img_url)
            elif img_url.startswith('https://') or img_url.startswith('http://'):
                pass
            else:
                continue

            response = requests.get(img_url)
            if response.status_code == 200:
                img_ext = os.path.splitext(img_url)[1][1:]  # Get the file extension
                if img_ext in ['png', 'jpeg', 'jpg', 'ico']:
                    with open(os.path.join(output_dir, 'img', os.path.basename(img_url)), 'wb') as file:
                        file.write(response.content)

    # Download videos
    video_links = soup.find_all('video', src=True)
    for video in video_links:
        video_url = urljoin(base_url, video['src'])
        response = requests.get(video_url)
        if response.status_code == 200:
            video_ext = os.path.splitext(video_url)[1][1:]  # Get the file extension
            if video_ext in ['mp4', 'webm', 'ogg']:
                with open(os.path.join(output_dir, 'video', os.path.basename(video_url)), 'wb') as file:
                    file.write(response.content)

    # Find and download other videos
    other_video_links = []
    for tag in soup.find_all(['a', 'link', 'script', 'img', 'iframe', 'button', 'form']):
        for attr in ['href', 'src', 'action']:
            url = tag.get(attr)
            if url:
                full_url = urljoin(base_url, url)
                if full_url not in other_video_links and full_url.endswith(('.mp4', '.webm', '.ogg')):
                    other_video_links.append(full_url)
    for video_url in other_video_links:
        response = requests.get(video_url)
        if response.status_code == 200:
            video_ext = os.path.splitext(video_url)[1][1:]  # Get the file extension
            if video_ext in ['mp4', 'webm', 'ogg']:
                with open(os.path.join(output_dir, 'video', os.path.basename(video_url)), 'wb') as file:
                    file.write(response.content)

def download_website(website_url):
    base_url = re.sub(r'^https?://', '', website_url).split('/')[0]
    domain = base_url

    # Create directories
    output_dir = os.path.join('output', 'others', 'website_stealer', domain)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'css'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'js'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'img'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'video'), exist_ok=True)

    # Download HTML
    response = requests.get(website_url)
    if response.status_code == 200:
        with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as file:
            file.write(response.text)

    # Download assets
    download_assets(website_url, website_url, output_dir)

    # Find and download all linked assets
    all_links = []
    def find_linked_assets(website_url, domain):
        nonlocal all_links
        soup = BeautifulSoup(requests.get(website_url).content, 'html.parser')
        for tag in soup.find_all(['a', 'link', 'script', 'img', 'iframe', 'button', 'form']):
            href = tag.get('href')
            src = tag.get('src')
            action = tag.get('action')
            if href:
                full_url = urljoin(website_url, href)
                if full_url not in all_links and domain in full_url and 'robots.txt' not in full_url:
                    all_links.append(full_url)
            if src:
                full_url = urljoin(website_url, src)
                if full_url not in all_links and domain in full_url and 'robots.txt' not in full_url:
                    all_links.append(full_url)
            if action:
                full_url = urljoin(website_url, action)
                if full_url not in all_links and domain in full_url and 'robots.txt' not in full_url:
                    all_links.append(full_url)
    find_linked_assets(website_url, domain)
    for link in all_links:
        download_assets(link, link, output_dir)

website_url = input("Website Url -> ")
if "https://" not in website_url and "http://" not in website_url:
    website_url = "https://" + website_url

download_website(website_url)

print("Download complete!")