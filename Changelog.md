# Changelog

## Version 1.0.6

* Added `get()` method to the bot class to retrieve configuration items from `plcord.json`

## version 1.0.6
* Bug fix: Corrected improper replacement of `mc` with `pl` in editor

## Version 1.0.0

* Removed FastSelect.
* Made a custom cog loader, now the object of a cog is now `plcord.Bot` instead of `discord.Bot`.
* Added `plcord.json` instead of passing the arguments direct to the bot class.
* change the `exec` method to `run`, token is now an optional argument.
* Added docstrings to all methods in the bot class.
* Added a custom error.
* Added `try-except` to the version checker.
* Added a full bot example for `plcord 1.0.0`.
* Added the `Log` class to the `__init__` so you can use the logger too.
