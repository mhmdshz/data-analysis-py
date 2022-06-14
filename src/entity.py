from operator import index
import pandas as pd
from .types import _FormatSaveFlie
from src.utils import myLogger


class Entity:
    commentsPath = "./files/AppsCommentsLessThan3yEn.pkl"

    def __init__(self) -> None:
        myLogger(level="info", msg="reading files...")
        pd.set_option("display.width", 70)
        self.comments: pd.DataFrame = pd.read_pickle(self.commentsPath)
        self.pd = pd

    def saveToCurrentFile(self, data: pd.DataFrame, to: _FormatSaveFlie, path: str):

        kwargs = {index: False} if to == "to_csv" else {} if to == "to_pickle" else {}

        myLogger(level="info", msg="saving file...")
        getattr(data, to)(path, **kwargs)

    def saveToOtherFile(self, data: pd.DataFrame, to: _FormatSaveFlie, name: str):

        kwargs = {index: False} if to == "to_csv" else {} if to == "to_pickle" else {}

        myLogger(level="info", msg="saving file...")

        getattr(data, to)(f"./files/{name}", **kwargs)
