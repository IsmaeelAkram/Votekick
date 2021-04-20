import discord
import random
import string
from discord.ext import commands
from utils import embed


class VotekickCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
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

        request_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        message = await ctx.channel.send(
            embed=embed.Embed(
                title="Vote started!",
                description=f"{ctx.author.mention} wants to kick {user.mention} for `{reason}`!",
                footer=f"Request ID: {request_id}"
            )
        )
        await message.add_reaction("✅")
        await message.add_reaction("❌")
