import discord
import dinocord as di
from dinocord.ext import Jsonparser

bot = di.Bot()
reader = Jsonparser("test.json")


@bot.slash_command(name="test")
async def test(ctx: discord.ApdiicationContext) -> None:
    await ctx.respond(reader.get("test"))
    await ctx.send(reader.get("age"))

if __name__ == "__main__":
    bot.run("token")
