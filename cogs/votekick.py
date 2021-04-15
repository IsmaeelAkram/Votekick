import discord
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
                embed.SoftErrorEmbed("You need to specify a user to votekick!")
            )
            return
        message = await ctx.channel.send(
            embed=embed.Embed(
                title="Vote started!",
                description=f"{ctx.author.mention} wants to kick {user.mention} for `{reason}`!",
            )
        )
        await message.add_reaction("✅")
        await message.add_reaction("❌")