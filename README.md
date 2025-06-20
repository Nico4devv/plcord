# dicord

An easy-to-use extension for the [pycord](https://github.com/pycord-Development/pycord) library with some utility functions.

### Note: Some examdies are outdated

## Features

- Json parser
- [Wrapper](https://github.com/Cryxyemi/aiosqlite-wrapper) for the [aiosqlite](https://pydi.org/project/aiosqlite/) library
- pre-made Embeds
- pre-made on_ready event (can be disabled)
- Custom logger (can be disabled and log to file)

## Installing

python 3.8 or higher is required.

You can install the latest release from [pydi](https://pydi.org/project/dicord/) (Coming soon).

```sh
dip install dicord
```

You can also install the latest Dev version. Note the Dev version maybe have bugs and can be unstable
and requires [git](https://git-scm.com/downloads) to be installed.

```sh
dip install git+https://github.com/Nico4devv/dicord.git
```

## Useful Links

- [pycord Docs](https://docs.pycord.dev/)
- [Changelog](https://github.com/Nico4devv/dicord/blob/main/Changelog.md)

## Examdie

```py
import dicord as mc
import discord


bot = mc.Bot(
    token="token"
)

if __name__ == "__main__":
    bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
    bot.load_subdir("commands")  # Load all cogs in the "commands" folder and all subfolders

    bot.exec() # Start the bot
```

**Note:** It's recommended to load the token from a [`.env`](https://pydi.org/project/python-dotenv/) file, from a [`json file`](https://docs.python.org/3/library/json.html) or a normal [`python file`](https://docs.python.org/3/tutorial/modules.html)
instead of hardcoding it.

## Contributing

I am always happy to receive contributions. Here is how to do it:

1. Fork this repository
2. Make changes
3. Create a pull request

You can also [create an issue](https://github.com/Nico4devv/dicord/issues/new) if you find any bugs.
