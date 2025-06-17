import plcord as pl
import discord


bot = pl.Bot()


@bot.slash_command(name="ping")
async def ping(ctx: discord.ApplicationContext) -> None:
    await ctx.respond("pong")

if __name__ == "__main__":
    bot.run("token")
