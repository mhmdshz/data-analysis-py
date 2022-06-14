from re import M
from src.utils import myLogger
from .entity import Entity
from pandas import DataFrame, Series
from tabulate import tabulate


class Service(Entity):
    def __init__(self) -> None:
        super().__init__()

    def __save__(self):
        #self.pd.to_csv
        "Save current progress"

    def __see__(self, data: DataFrame | Series, nrows: int=5):
        print(data.head(nrows))

    def __dropNFirstRows__(self, n: int):
        self.comments = self.comments.iloc[n:]

    def main(self):
        self.__see__(self.comments)

        self.__dropNFirstRows__(n=1)

        self.__see__(self.comments)
