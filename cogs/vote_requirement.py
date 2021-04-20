import discord
from discord.ext import commands
from utils import embed
from tinydb import TinyDB, where


class VoteRequirement(commands.Cog):
    def __init__(self, bot: commands.Bot, db: TinyDB):
        self.db = db
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def vote_requirement(self, ctx: commands.Context, count: int):
        vote_requirement_table = self.db.table("vote_requirement")
        count_search = vote_requirement_table.search(where("guild_id") == ctx.guild.id)
        if len(count_search) == 0:
            vote_requirement_table.insert({"guild_id": ctx.guild.id, "count": count})
        else:
            vote_requirement_table.remove(where("guild_id") == ctx.guild.id)
            vote_requirement_table.insert({"guild_id": ctx.guild.id, "count": count})

        await ctx.channel.send(
            embed=embed.Embed(
                description=f"Vote count requirement changed to `{count}`"
            )
        )
