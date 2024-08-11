import requests
import discord
from discord.ext import commands, tasks

BASE_LINK = "https://clientsettings.roblox.com/v2/client-version"
WINDOWS_VERSION =  requests.get(f"{BASE_LINK}/WindowsPlayer").json()["version"]
MAC_VERSION = requests.get(f"{BASE_LINK}/MacPlayer").json()["version"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready!")
    await roblox_check.start()

@tasks.loop(seconds=10)
async def roblox_check():
    global WINDOWS_VERSION
    global MAC_VERSION
    global BASE_LINK
    channel = bot.get_guild(1271217438272520282).get_channel(1271217977257234512)
    windows_req = requests.get(f"{BASE_LINK}/WindowsPlayer").json()["version"]
    mac_req = requests.get(f"{BASE_LINK}/MacPlayer").json()["version"]
    while True:
        if windows_req != WINDOWS_VERSION:
            embed = discord.Embed(
                title="Roblox Update",
                description="Roblox has updated their windows client", 
                colour=discord.Colour.magenta(),
                timestamp=discord.utils.utcnow(),
            )
            embed.set_footer(text="Made by twotap")
            embed.add_field(name="Old Version", value=WINDOWS_VERSION, inline=True)
            embed.add_field(name="New Version", value=windows_req, inline=True)
            await channel.send(embed=embed)
            WINDOWS_VERSION = windows_req
            continue

        if mac_req != MAC_VERSION:
            embed = discord.Embed(
                title="Roblox Update",
                description="Roblox has updated their mac client", 
                colour=discord.Colour.magenta(),
                timestamp=discord.utils.utcnow(),
            )
            embed.set_footer(text="Made by twotap")
            embed.add_field(name="Old Version", value=MAC_VERSION, inline=True)
            embed.add_field(name="New Version", value=mac_req, inline=True)
            await channel.send(embed=embed)
            MAC_VERSION = mac_req
        
bot.run("TOKEN")