import pandas as pd

from src.utils import myLogger


class Entity:
    def __init__(self) -> None:
        myLogger(level="info", msg="reading files...")
        pd.set_option("display.width", 70)
        self.comments = pd.read_csv("./files/AppslessThan3yCommentsDateEnglish.csv", nrows=200, usecols=["appId", "en"])
        self.pd = pd
