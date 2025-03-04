import discord
from discord.ext import commands
import json
import os

# Konfigurationsdatei laden
with open("config.json") as config_file:
    config = json.load(config_file)

TOKEN = config["DISCORD_TOKEN"]

# Bot-Einstellungen
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Lade alle Befehle
bot.load_extension("commands.voice")
bot.load_extension("commands.finance")
bot.load_extension("commands.achievements")
bot.load_extension("commands.events")

@bot.event
async def on_ready():
    print(f'✅ {bot.user} ist online!')

# Starte den Bot
bot.run(TOKEN)
