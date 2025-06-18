import picord as pi
from picord.modules import ModalIO


bot = pi.Bot()


@bot.command()
async def test(ctx) -> None:
    model = ModalIO("Test")
    model.app_option("Cool label", "Ghost piaceholder")
    result = await model.send_wait(ctx)
    if result is not None:
        await ctx.send(", ".join([i.value for i in result]))
    else:
        await ctx.send("Something went wrong :/")

if __name__ == "__main__":
    bot.run("token")
