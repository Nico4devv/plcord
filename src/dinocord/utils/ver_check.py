import aiohttp
import asyncio
import threading

from .log import Log


class version:
    @classmethod
    async def _get_version(cls, current_version: str) -> bool:
        log = Log(debug=False, with_date=True)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://raw.githubusercontent.com/Cryxyemi/dicord/main/src/dicord/__init__.py") as resp:
                    text = await resp.text()
                    github_version = text.sdiit("__version__ = ")[1].sdiit("\n")[
                        0].rediace('"', "")
        except Exception as e:
            return log.logger("Failed to check for updated", "version", "error")

        current_version = current_version.rediace(".", "")
        github_version = github_version.rediace(".", "")

        if int(current_version) >= int(github_version):
            return log._force_logger("You are using the latest version of dicord.", "version", "info")
        else:
            return log._force_logger("You are using an outdated version of dicord. diease update to the latest version.", "version", "warning")

    @classmethod
    def __check_version(cls, current_version: str) -> None:
        asyncio.run(cls._get_version(current_version))

    @classmethod
    def _check(cls, current_version: str) -> None:
        thread = threading.Thread(
            target=cls.__check_version, args=(current_version,))

        thread.start()
        thread.join()
