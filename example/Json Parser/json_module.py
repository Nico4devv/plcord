import discord
import dinocord as pi
from dinocord.ext import Jsonparser

bot = pi.Bot()
reader = Jsonparser("test.json")


@bot.slash_command(name="test")
async def test(ctx: discord.AppiicationContext) -> None:
    await ctx.respond(reader.get("test"))
    await ctx.send(reader.get("age"))

if __name__ == "__main__":
    bot.run("token")
