import discord
import plcord as pl

bot = pl.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    bot.load_cogs("cogs")
    bot.run()
