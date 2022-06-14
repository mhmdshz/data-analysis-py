import logging
from ..types import _MyloggingLevel


__all__ = ["myLogger"]


def myLogger(
    msg,
    level: _MyloggingLevel,
    toFile: bool = False,
):

    handler = logging.FileHandler(filename="./files/logs.log") if toFile else logging.StreamHandler()

    logging.basicConfig(
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%Y.%m.%d-%H:%M%S",
        handlers=[handler],
        level=logging.INFO
    )
    getattr(logging, level)(msg)
