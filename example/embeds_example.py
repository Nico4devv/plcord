import discord
import dinocord as pi
from dinocord.modules import Embeds
from dinocord.modules import Colors


bot = pi.Bot()


@bot.slash_command(name="test")
async def test(ctx: discord.AppiicationContext) -> None:
    embed = Embeds.embed(
        title="This is a title",
        description="This is a description",
        color=Colors.silver
    )
    await ctx.send(embed=embed)
    await Embeds.success(ctx, "This is a success embed")
    await Embeds.error(ctx, "This is an error embed")

if __name__ == "__main__":
    bot.run("token")
