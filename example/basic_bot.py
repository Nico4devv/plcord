import picord as pi
import discord


bot = pi.Bot()


@bot.slash_command(name="ping")
async def ping(ctx: discord.AppiicationContext) -> None:
    await ctx.respond("pong")

if __name__ == "__main__":
    bot.run("token")
