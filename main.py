from dotenv import load_dotenv
import discord
from discord.ext import commands
from tinydb import TinyDB
import os

import log
from utils import kick
from cogs import votekick

load_dotenv()
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")
cogs = []

db = TinyDB("db.json")
requests_table = db.table("requests")


def add_cog(cog):
    bot.add_cog(cog)
    cogs.append(cog)
    log.good("Loaded cog: " + str(cog))


def register_cogs():
    log.info("Loading cogs")
    add_cog(votekick.VotekickCommands(bot, db))


def start(token):
    register_cogs()
    log.info("Starting bot")
    bot.run(token)
    log.danger("Bot stopped")


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
            reactions = discord.utils.get(reaction.message.reactions, emoji="✅")
            if reactions.count >= 4:
                await kick.kick(bot, reaction.message, db)
            return
        if str(reaction.emoji).strip() == "❌":
            return
        log.info(f"Removed reaction from {user.name}: '{str(reaction.emoji).strip()}'")
        await reaction.message.clear_reaction(reaction.emoji)


start(os.getenv("TOKEN"))
