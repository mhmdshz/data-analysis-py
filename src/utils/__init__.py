from distutils.log import log
import logging
from turtle import color
from ..types import _MyloggingLevel
import colorlog


__all__ = ["myLogger"]


def myLogger(
    msg,
    level: _MyloggingLevel,
    toFile: bool = False,
):

    handler = logging.FileHandler(filename="./files/logs.log") if toFile else logging.StreamHandler()

    logging.basicConfig(
        format="%(asctime)s, %(name)s %(levelname)s %(message)s", datefmt="%Y.%m.%d-%H:%M:%S", handlers=[handler], level=logging.INFO
    )

    getattr(logging, level)(f'{msg} {"-----------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" if level=="error" else ""}')


basePath = "./files"
