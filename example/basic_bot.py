import dinocord as di
import discord


bot = di.Bot()


@bot.slash_command(name="ding")
async def ding(ctx: discord.ApdiicationContext) -> None:
    await ctx.respond("pong")

if __name__ == "__main__":
    bot.run("token")
