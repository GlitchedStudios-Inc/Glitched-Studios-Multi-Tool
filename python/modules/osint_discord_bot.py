from os import name
import discord
from discord import embeds
from discord import user
from discord.ext import commands, tasks
from discord.guild import Guild
from discord import app_commands
from discord.interactions import Interaction
from discord.invite import Invite
from discord.ui import View, Button, button, Select
from discord import File
import json
import random
import asyncio
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
import dns.resolver
import aiohttp
import scapy

with open('settings/configs/Osint Bot Config.json') as f:
    config = json.load(f)

TOKEN = config['bottoken']
bot = commands.Bot(command_prefix='g?',
                   intents=discord.Intents.all(),
                   help_command=None)


async def change_status():
    while True:
        status = random.choice(presence_option)
        activity = random.choice(activity_options)
        await bot.change_presence(status=status, activity=activity)
        await asyncio.sleep(10)


presence_option = [
    discord.Status.online,
    discord.Status.idle,  
    discord.Status.dnd, 
]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    global activity_options
    activity_options = [
        discord.Activity(
            name="Glitched Studios Discord Osint Bot",
            type=discord.ActivityType.playing,
            url="https://discord.gg/glitched-studios",
            state=f"🛠 Helping Your Members | {len(bot.guilds)}",
        ), 
        discord.Activity(
            name="Glitched Studios Discord Osint Bot",
            type=discord.ActivityType.playing,
            url="https://discord.gg/glitched-studios",
            state=f"🛠 Running Your Servers | {len(bot.guilds)}",
        ), 
        discord.Activity(
            name="Glitched Studios Discord Osint Bot",
            type=discord.ActivityType.playing,
            url="https://discord.gg/glitched-studios",
            state=f"🛠 Watching You Sleep | {len(bot.guilds)}",
        )  
    ]
    sync = await bot.tree.sync()
    print(f"Synced {len(sync)} commands")


@bot.tree.command(
    name="ip2info",
    description="Get information about an IP address (auto not show)")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def ipinfouser(interaction: discord.Interaction,
                     ip: str,
                     showornot: bool = False):
    response = requests.get(f'http://ip-api.com/json/{ip}?fields=66846719')

    if response.status_code != 200:
        await interaction.response.send_message(
            f'Failed to retrieve IP information. Status code: {response.status_code}'
        )
        return

    try:
        api = response.json()
    except json.JSONDecodeError:
        await interaction.response.send_message(
            'Failed to parse response as JSON.')
        return

    iponoroff = True
    if showornot == False:
        iponoroff = True
    if showornot == True:
        iponoroff = False

    embed = discord.Embed(title=f'IP Information for {ip}',
                          color=discord.Color.random())
    embed.add_field(name='Status', value=f"```{api['status']}```", inline=True)
    embed.add_field(name='Continent',
                    value=f"```{api['continent']}```",
                    inline=True)
    embed.add_field(name='Continent Code',
                    value=f"```{api['continentCode']}```",
                    inline=True)
    embed.add_field(name='Country',
                    value=f"```{api['country']}```",
                    inline=True)
    embed.add_field(name='Country Code',
                    value=f"```{api['countryCode']}```",
                    inline=True)
    embed.add_field(name='Region', value=f"```{api['region']}```", inline=True)
    embed.add_field(name='Region Name',
                    value=f"```{api['regionName']}```",
                    inline=True)
    embed.add_field(name='City', value=f"```{api['city']}```", inline=True)
    embed.add_field(name='Zip', value=f"```{api['zip']}```", inline=True)
    embed.add_field(name='Latitude', value=f"```{api['lat']}```", inline=True)
    embed.add_field(name='Longitude', value=f"```{api['lon']}```", inline=True)
    embed.add_field(name='Timezone',
                    value=f"```{api['timezone']}```",
                    inline=True)
    embed.add_field(name='ISP', value=f"```{api['isp']}```", inline=True)
    embed.add_field(name='Organization',
                    value=f"```{api['org']}```",
                    inline=True)
    embed.add_field(name='AS', value=f"```{api['as']}```", inline=True)
    embed.add_field(name='Query', value=f"```{api['query']}```", inline=True)
    embed.add_field(
        name='Location URL',
        value=
        f"https://www.google.com/maps/search/?api=1&query={api['lat']},{api['lon']}",
        inline=True)

    await interaction.response.send_message(embed=embed, ephemeral=iponoroff)



@bot.tree.command(name="website2info", description="Gets Info From A Website")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def idlookup(interaction: discord.Interaction,
                   dom: str,
                   showornot: bool = False):
    urldomain = 'https://api.leaked.wiki/host2ip?domain=' + dom
    kyspython = requests.get(urldomain)
    inolikepy = kyspython.json()
    slient = True
    if showornot == False:
        slient = True
    if showornot == True:
        slient = False
    if inolikepy.get('success') == True:
        embed = discord.Embed(title=f'Domain Ip For {dom}',
                              color=discord.Color.random())
        embed.add_field(name="IP",
                        value=f"```{inolikepy.get('ip')}```",
                        inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=slient)
    else:
        await interaction.response.send_message("Invalid domain",
                                                ephemeral=slient)

@bot.tree.command(name="email2info",
                  description="Get information about an email address")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def email_info(interaction: discord.Interaction, email: str):
    try:

        def get_email_info(email):
            info = {}
            try:
                domain_all = email.split('@')[-1]
            except:
                domain_all = None

            try:
                name = email.split('@')[0]
            except:
                name = None

            try:
                domain = re.search(r"@([^@.]+)\.", email).group(1)
            except:
                domain = None
            try:
                tld = f".{email.split('.')[-1]}"
            except:
                tld = None

            try:
                mx_records = dns.resolver.resolve(domain_all, 'MX')
                mx_servers = [str(record.exchange) for record in mx_records]
                info["mx_servers"] = mx_servers
            except dns.resolver.NoAnswer:
                info["mx_servers"] = None
            except dns.resolver.NXDOMAIN:
                info["mx_servers"] = None

            try:
                spf_records = dns.resolver.resolve(domain_all, 'SPF')
                info["spf_records"] = [str(record) for record in spf_records]
            except dns.resolver.NoAnswer:
                info["spf_records"] = None
            except dns.resolver.NXDOMAIN:
                info["spf_records"] = None

            try:
                dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}',
                                                     'TXT')
                info["dmarc_records"] = [
                    str(record) for record in dmarc_records
                ]
            except dns.resolver.NoAnswer:
                info["dmarc_records"] = None
            except dns.resolver.NXDOMAIN:
                info["dmarc_records"] = None

            if "mx_servers" in info:
                for server in info["mx_servers"]:
                    if "google.com" in server:
                        info["google_workspace"] = True
                    elif "outlook.com" in server:
                        info["microsoft_365"] = True

            try:
                response = requests.get(
                    f"https://api.mailgun.net/v4/address/validate?address={email}",
                    auth=("api", "YOUR_MAILGUN_API_KEY"))
                data = response.json()
                info["mailgun_validation"] = data
            except Exception as e:
                info["mailgun_validation"] = {"error": str(e)}

            return info, domain_all, domain, tld, name

        info, domain_all, domain, tld, name = get_email_info(email)

        try:
            mx_servers = info["mx_servers"]
            mx_servers = ' / '.join(mx_servers)
        except Exception as e:
            mx_servers = None

        try:
            spf_records = info["spf_records"]
        except:
            spf_records = None

        try:
            dmarc_records = info["dmarc_records"]
            dmarc_records = ' / '.join(dmarc_records)
        except:
            dmarc_records = None

        try:
            google_workspace = info["google_workspace"]
        except:
            google_workspace = None

        try:
            mailgun_validation = info["mailgun_validation"]
            mailgun_validation = ' / '.join(mailgun_validation)
        except:
            mailgun_validation = None

        embed = discord.Embed(title="Email Information",
                              color=discord.Color.random())
        embed.add_field(name="Email", value=f"```{email}```", inline=True)
        embed.add_field(name="Name", value=f"```{name}```", inline=True)
        embed.add_field(name="Domain", value=f"```{domain}```", inline=True)
        embed.add_field(name="Tld", value=f"```{tld}```", inline=True)
        embed.add_field(name="Domain All",
                        value=f"```{domain_all}```",
                        inline=True)
        embed.add_field(name="Spf", value=f"```{spf_records}```", inline=True)
        embed.add_field(name="Dmarc",
                        value=f"```{dmarc_records}```",
                        inline=True)
        embed.add_field(name="Workspace",
                        value=f"```{str(google_workspace)}```",
                        inline=True)
        embed.add_field(name="Mailgun",
                        value=f"```{mailgun_validation}```",
                        inline=True)

        await interaction.response.send_message(embed=embed)

    except Exception as e:
        await interaction.response.send_message("An error occurred: " + str(e))


@bot.tree.command(name="roblox_user2info", description="Get information about a Roblox user")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def roblox_user_info(interaction: discord.Interaction, username: str):
    try:
        response = requests.post("https://users.roblox.com/v1/usernames/users",
                                 json={
                                     "usernames": [username],
                                     "excludeBannedUsers": "true"
                                 })

        data = response.json()

        if not data["data"]:
            await interaction.response.send_message("Invalid username or user not found!")
            return

        user_id = data["data"][0]["id"]

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        user_info = user_info_response.json()

        userid = user_info.get('id', "None")
        display_name = user_info.get('displayName', "None")
        username = user_info.get('name', "None")
        description = user_info.get('description', "None")
        created_at = user_info.get('created', "None")
        is_banned = user_info.get('isBanned', "None")
        external_app_display_name = user_info.get('externalAppDisplayName', "None")
        has_verified_badge = user_info.get('hasVerifiedBadge', "None")
        avatar_response = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=48x48&format=Png&isCircular=true")
        avatar_data = avatar_response.json()
        avatar_url = avatar_data["data"][0]["imageUrl"]
        friends_response = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends/count")
        friends_count = friends_response.json()["count"]
        followers_response = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/followers/count")
        followers_count = followers_response.json()["count"]
        status_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}/status")
        status_data = status_response.json()
        status = status_data.get('status', "None")
        game_stats_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}/game-stats")
        game_stats_data = game_stats_response.json()
        game_stats = game_stats_data.get('stats', [])

        embed = discord.Embed(title="Roblox User Information", color=discord.Color.random())
        embed.set_thumbnail(url=avatar_url)

        embed.add_field(name="**Username**", value=f"`{username}`", inline=False)
        embed.add_field(name="**Id**", value=f"`{userid}`", inline=False)
        embed.add_field(name="**Display Name**", value=f"`{display_name}`", inline=False)

        embed.add_field(name="**Description**", value=f"`{description}`", inline=False)
        embed.add_field(name="**Created**", value=f"`{created_at}`", inline=False)
        embed.add_field(name="**Banned**", value=f"`{is_banned}`", inline=False)

        embed.add_field(name="**External Name**", value=f"`{external_app_display_name}`", inline=False)
        embed.add_field(name="**Verified Badge**", value=f"`{has_verified_badge}`", inline=False)

        embed.add_field(name="**Friends**", value=f"`{friends_count}`", inline=False)
        embed.add_field(name="**Followers**", value=f"`{followers_count}`", inline=False)

        embed.add_field(name="**Status**", value=f"`{status}`", inline=False)

        game_stats_str = ""
        for stat in game_stats:
            game_stats_str += f"**{stat['name']}:** `{stat['value']}`\n"
        embed.add_field(name="**Game Stats**", value=game_stats_str, inline=False)

        embed.set_footer(
            text=f"View {username}'s profile: https://www.roblox.com/users/{user_id}/profile",
            icon_url="https://www.roblox.com/favicon.ico"
        )

        await interaction.response.send_message(embed=embed)

    except requests.exceptions.RequestException as e:
        await interaction.response.send_message(f"Error: Unable to retrieve user information! ({e})")
    except json.JSONDecodeError as e:
        await interaction.response.send_message(f"Error: Invalid JSON response! ({e})")
    except Exception as e:
        await interaction.response.send_message(f"Error: Unknown error! ({e})")

@bot.tree.command(name="webhook_spammer",
                  description="Spam a Discord webhook with a message")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def webhook_spammer(
        interaction: discord.Interaction,
        webhook_url: str,
        message: str,
        threads_number: int,
        username: str = "Glitched Studios Osint Bot Webhook Spammer",
        avatar: str = None):
    try:
        headers = {'Content-Type': 'application/json'}
        payload = {
            'content': message,
            'username': username,
            'avatar_url': avatar
        }

        async def send_webhook():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                            webhook_url, headers=headers,
                            data=json.dumps(payload)) as response:
                        if response.status == 204:
                            print(
                                f"{discord.utils.format_dt(discord.utils.utcnow(), style='f')} | Message: {message} | Status: Send"
                            )
                        elif response.status == 429:
                            print(
                                f"{discord.utils.format_dt(discord.utils.utcnow(), style='f')} | Message: {message} | Status: Rate Limit"
                            )
                        else:
                            print(
                                f"{discord.utils.format_dt(discord.utils.utcnow(), style='f')} | Message: {message} | Status: Error"
                            )
            except Exception as e:
                print(
                    f"{discord.utils.format_dt(discord.utils.utcnow(), style='f')} | Message: {message} | Status: Error - {str(e)}"
                )

        async def request():
            tasks = []
            for _ in range(threads_number):
                task = asyncio.create_task(send_webhook())
                tasks.append(task)
            await asyncio.gather(*tasks)

        await interaction.response.send_message("Webhook spammer started!")
        await request()
        await interaction.response.send_message("Webhook spammer d!")
    except Exception as e:
        await interaction.response.send_message("An error occurred: " + str(e))


@bot.tree.command(name="delete_webhook",
                  description="Delete a Discord webhook")
@app_commands.describe(webhook_url="The URL of the webhook")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def delete_webhook(interaction: discord.Interaction, webhook_url: str):
    try:
        print(
            f"{discord.utils.format_dt(discord.utils.utcnow(), style='f')} | Delete Webhook: {webhook_url}"
        )

        requests.delete(webhook_url)

        await interaction.response.send_message(f"Webhook deleted.")
    except aiohttp.ClientResponseError as e:
        if e.status == 404:
            await interaction.response.send_message(f"Webhook not found.")
        else:
            await interaction.response.send_message(
                f"An error occurred: {str(e)}")
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}")
@bot.tree.command(name="webhook2info",
                  description="Get information about a Discord webhook")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(webhook_url="The URL of the webhook")
async def webhook_info(interaction: discord.Interaction, webhook_url: str):
    try:
        headers = {
            'Content-Type': 'application/json',
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(webhook_url, headers=headers) as response:
                webhook_info = await response.json()

        embed = discord.Embed(title="Webhook Information",
                              color=discord.Color.random())

        embed.add_field(name="ID", value=webhook_info['id'], inline=False)
        embed.add_field(name="Token",
                        value=webhook_info['token'],
                        inline=False)
        embed.add_field(name="Name", value=webhook_info['name'], inline=False)
        embed.add_field(name="Avatar",
                        value=webhook_info['avatar'],
                        inline=False)
        embed.add_field(
            name="Type",
            value="Bot" if webhook_info['type'] == 1 else "User Webhook",
            inline=False)
        embed.add_field(name="Channel ID",
                        value=webhook_info['channel_id'],
                        inline=False)
        embed.add_field(name="Server ID",
                        value=webhook_info['guild_id'],
                        inline=False)

        if 'user' in webhook_info:
            user_info = webhook_info['user']

            embed.add_field(name="User ID",
                            value=user_info['id'],
                            inline=False)
            embed.add_field(name="Username",
                            value=user_info['username'],
                            inline=False)
            embed.add_field(name="Display Name",
                            value=user_info['global_name'],
                            inline=False)
            embed.add_field(name="Discriminator",
                            value=user_info['discriminator'],
                            inline=False)
            embed.add_field(name="Avatar",
                            value=user_info['avatar'],
                            inline=False)
            embed.add_field(
                name="Flags",
                value=
                f"{user_info['flags']} Public: {user_info['public_flags']}",
                inline=False)
            embed.add_field(name="Accent Color",
                            value=user_info['accent_color'],
                            inline=False)
            embed.add_field(name="Avatar Decoration",
                            value=user_info['avatar_decoration_data'],
                            inline=False)
            embed.add_field(name="Banner Color",
                            value=user_info['banner_color'],
                            inline=False)

        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}")



@bot.tree.command(name="serverinvite2info", description="Get information about a Discord server")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def serverinfo(interaction: discord.Interaction, invite: str):
    try:
        invite_code = invite.split("/")[-1]
    except:
        invite_code = invite

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        data = response.json()
        try:
            type_value = data['type']
        except:
            type_value= "None"
        try:
            code_value = data['code']
        except:
            code_value = "None"
        try:
            inviter_id = data['inviter']['id']
        except:
            inviter_id = "None"
        try:
            inviter_username = data['inviter']['username']
        except:
            inviter_username = "None"
        try:
            inviter_avatar = data['inviter']['avatar']
        except:
            inviter_avatar = "None"
        try:
            inviter_discriminator = data['inviter']['discriminator']
        except:
            inviter_discriminator = "None"
        try:
            inviter_public_flags = data['inviter']['public_flags']
        except:
            inviter_public_flags = "None"
        try:
            inviter_flags = data['inviter']['flags']
        except:
            inviter_flags = "None"
        try:
            inviter_banner = data['inviter']['banner']
        except:
            inviter_banner = "None"
        try:
            inviter_accent_color = data['inviter']['accent_color']
        except:
            inviter_accent_color = "None"
        try:
            inviter_global_name = data['inviter']['global_name']
        except:
            inviter_global_name = "None"
        try:
            inviter_banner_color = data['inviter']['banner_color']
        except:
            inviter_banner_color = "None"
        try:
            expires_at = data['expires_at']
        except:
            expires_at = "None"
        try:
            flags = data['flags']
        except:
            flags = "None"
        try:
            server_id = data['guild_id']
        except:
            server_id = "None"
        try:
            server_name = data['guild']['name']
        except:
            server_name = "None"
        try:
            server_icon = data['guild']['icon']
        except:
            server_icon = "None"
        try:
            server_features = data['guild']['features']
        except:
            server_features = "None"
        try:
            server_verification_level = data['guild']['verification_level']
        except:
            server_verification_level = "None"
        try:
            server_nsfw_level = data['guild']['nsfw_level']
        except:
            server_nsfw_level = "None"
        try:
            server_nsfw = data['guild']['nsfw']
        except:
            server_nsfw = "None"
        try:
            server_premium_subscription_count = data['guild']['premium_subscription_count']
        except:
            server_premium_subscription_count = "None"
        try:
            channel_id = data['channel']['id']
        except:
            channel_id = "None"
        try:
            channel_type = data['channel']['type']
        except:
            channel_type = "None"
        try:
            channel_name = data['channel']['name']
        except:
            channel_name = "None"
        embed1 = discord.Embed(title="Server Information", color=discord.Color.random())
        embed1.add_field(name="Invitation", value=invite, inline=False)
        embed1.add_field(name="Type", value=type_value, inline=False)
        embed1.add_field(name="Code", value=code_value, inline=False)
        embed1.add_field(name="Expired", value=expires_at, inline=False)
        embed1.add_field(name="Server ID", value=server_id, inline=False)
        embed1.add_field(name="Server Name", value=server_name, inline=False)
        embed1.add_field(name="Channel ID", value=channel_id, inline=False)
        embed1.add_field(name="Channel Name", value=channel_name, inline=False)
        embed1.add_field(name="Channel Type", value=channel_type, inline=False)
        embed1.add_field(name="Server Icon", value=server_icon, inline=False)
        embed1.add_field(name="Server Features", value=server_features, inline=False)
        embed1.add_field(name="Server NSFW Level", value=server_nsfw_level, inline=False)
        embed1.add_field(name="Server NSFW", value=server_nsfw, inline=False)
        embed1.add_field(name="Flags", value=flags, inline=False)
        embed2 = discord.Embed(title="Server Information (continued)", color=discord.Color.random())
        embed2.add_field(name="Server Verification Level", value=server_verification_level, inline=False)
        embed2.add_field(name="Server Premium Subscription Count", value=server_premium_subscription_count, inline=False)
        embed3 = discord.Embed(title="Inviter Information", color=discord.Color.random())
        embed3.add_field(name="ID", value=inviter_id, inline=False)
        embed3.add_field(name="Username", value=inviter_username, inline=False)
        embed3.add_field(name="Global Name", value=inviter_global_name, inline=False)
        embed3.add_field(name="Avatar", value=inviter_avatar, inline=False)
        embed3.add_field(name="Discriminator", value=inviter_discriminator, inline=False)
        embed3.add_field(name="Public Flags", value=inviter_public_flags, inline=False)
        embed3.add_field(name="Flags", value=inviter_flags, inline=False)
        embed3.add_field(name="Banner", value=inviter_banner, inline=False)
        embed3.add_field(name="Accent Color", value=inviter_accent_color, inline=False)
        embed3.add_field(name="Banner Color", value=inviter_banner_color, inline=False)
        await interaction.response.send_message(embeds=[embed1, embed2, embed3])
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, world!')


try:
    bot.run(TOKEN)
except discord.errors.LoginFailure:
    print(
        "Invalid token. Please put a token in settings/configs/Osint Bot Config.json or get a different bot token"
    )
