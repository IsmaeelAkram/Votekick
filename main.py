from dotenv import load_dotenv
import discord
from discord.ext import commands
import chalk
import os

import log
from utils import embed
from cogs import votekick

load_dotenv()
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")
cogs = []


def add_cog(cog):
    bot.add_cog(cog)
    cogs.append(cog)
    print(chalk.cyan(f"Loaded cog: {cog}"))


def register_cogs():
    print(chalk.yellow("Loading cogs..."))
    add_cog(votekick.VotekickCommands(bot))


def start(token):
    register_cogs()
    log.info("Starting bot")
    bot.run(token)
    log.good("Bot started")


@bot.event
async def on_ready():
    log.good("Bot is ready")
    await bot.change_presence(
        activity=discord.Game("!votekick | votekick.ismaeelakram.com")
    )
    log.good("Presence changed")


start(os.getenv("TOKEN"))