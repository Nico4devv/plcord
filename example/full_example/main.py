import discord
import dinocord as di

bot = di.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    bot.load_cogs("cogs")
    bot.run()
