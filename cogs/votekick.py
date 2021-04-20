import discord
import random
import string
from discord.ext import commands
from utils import embed
from tinydb import TinyDB


class VotekickCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, db: TinyDB):
        self.db = db
        self.bot = bot

    @commands.command(aliases=["vk"])
    async def votekick(
        self, ctx: commands.Context, user: discord.Member, *, reason="no reason"
    ):
        if not user:
            await ctx.channel.send(
                embed=embed.SoftErrorEmbed("You need to specify a user to votekick!")
            )
            return
        if user.bot:
            await ctx.channel.send(
                embed=embed.SoftErrorEmbed("You cannot votekick bots.")
            )
            return
        if user.id == ctx.author.id:
            await ctx.channel.send(
                embed=embed.SoftErrorEmbed("You cannot votekick yourself.")
            )
            return

        request_id = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(16)
        )
        self.db.table("requests").insert(
            {
                "request_id": request_id,
                "user_id": user.id,
                "author_id": ctx.author.id,
                "guild_id": ctx.guild.id,
                "reason": reason,
            }
        )
        message = await ctx.channel.send(
            embed=embed.Embed(
                title="Vote started!",
                description=f"{ctx.author.mention} wants to kick {user.mention} for `{reason}`!",
                footer=f"Request ID: {request_id}",
            )
        )
        await message.add_reaction("✅")
