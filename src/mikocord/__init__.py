from .modules import (
    Embeds,
    ModalIO,
    Colors,
)
from .ext import (
    JsonParser,
    Database
)
from .utils.log import Log
from .utils.ver_check import version
from .bot import Bot

__title__ = "plcord"
__author__ = "Cryxyemi"
__license__ = "MIT"
__version__ = "1.0.5"


version._check(__version__)
