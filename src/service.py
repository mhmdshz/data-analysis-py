from re import M, T
from src.utils import myLogger
from .entity import Entity
from pandas import DataFrame, Series
from tabulate import tabulate


class Service(Entity):
    def __init__(self) -> None:
        super().__init__()

    def __see__(self, data: DataFrame | Series, nrows: int = 5):
        print(data.head(nrows))

    def __dropNFirstRows__(self, n: int):
        self.comments = self.comments.iloc[n:]

    def main(self):
        self.__see__(self.comments)

        
        # logic here


        self.__see__(self.comments)
