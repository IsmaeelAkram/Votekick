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
    log.good("Loaded cog: " + str(cog))


def register_cogs():
    log.info("Loading cogs")
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


@bot.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    if reaction.message.author.id == bot.user.id:
        if str(reaction.emoji).strip() == "✅":
            return
        if str(reaction.emoji).strip() == "❌":
            return
        log.info(f"Removed reaction from {user.name}: '{str(reaction.emoji).strip()}'")
        await reaction.message.clear_reaction(reaction.emoji)


start(os.getenv("TOKEN"))