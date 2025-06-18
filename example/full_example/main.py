import discord
import picord as pi

bot = pi.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    bot.load_cogs("cogs")
    bot.run()
