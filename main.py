from dotenv import load_dotenv
import discord
from discord.ext import commands
from tinydb import TinyDB, where
import os

import log
from utils import kick
from cogs import votekick, vote_requirement

load_dotenv()
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")
cogs = []

db = TinyDB("db.json")
requests_table = db.table("requests")
vote_requirement_table = db.table("vote_requirement")


def add_cog(cog):
    bot.add_cog(cog)
    cogs.append(cog)
    log.good("Loaded cog: " + str(cog))


def register_cogs():
    log.info("Loading cogs")
    add_cog(votekick.VotekickCommands(bot, db))
    add_cog(vote_requirement.VoteRequirement(bot, db))


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
            try:
                vote_requirement_count = vote_requirement_table.search(
                    where("guild_id") == reaction.message.guild.id
                )[0]["count"]
            except:
                vote_requirement_count = 3
            reactions = discord.utils.get(reaction.message.reactions, emoji="✅")
            if reactions.count >= vote_requirement_count:
                await kick.kick(bot, reaction.message, db)
        else:
            log.info(
                f"Removed reaction from {user.name}: '{str(reaction.emoji).strip()}'"
            )
            await reaction.message.clear_reaction(reaction.emoji)


start(os.getenv("TOKEN"))
