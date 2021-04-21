import discord


def Embed(
    description="",
    image=None,
    title="",
    color=0x10C42E,
    footer="",
):
    return discord.Embed(
        description=description, image=image, title=title, color=color
    ).set_footer(text=footer)


def SoftErrorEmbed(error):
    return discord.Embed(title="Oops!", description=error, color=0xD13F3F)
