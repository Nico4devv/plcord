from .modules import (
    Embeds,
    ModalIO,
    Colors,
)
from .ext import (
    Jsonparser,
    Database
)
from .utils.log import Log
from .utils.ver_check import version
from .bot import Bot

__title__ = "dicord"
__author__ = "Cryxyemi"
__license__ = "MIT"
__version__ = "1.0.6"


version._check(__version__)
