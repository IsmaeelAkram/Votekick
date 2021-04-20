import discord
from discord.ext import commands
from tinydb import TinyDB, where
from utils import embed


async def kick(bot: commands.Bot, vote_message: discord.Message, db: TinyDB):
    request_id = (
        vote_message.embeds[0].footer.text.replace("Request ID: ", "").split("|")[0]
    )
    request = db.table("requests").search(where("request_id") == request_id)[0]
    user = await bot.fetch_user(request["user_id"])

    await vote_message.guild.kick(user, reason=request["reason"])
    await vote_message.channel.send(
        embed=embed.Embed(
            description=f"Kicked {user.mention} for `{request['reason']}.`",
            footer="Request ID: " + request_id,
        )
    )
