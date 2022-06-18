from tkinter import S
from src.utils import myLogger
from .entity import Entity
from pandas import DataFrame, Series
from pandas._typing import Renamer
import matplotlib.pyplot as plt
from typing import Sequence, List
from .types import _DFname


class Service(Entity):
    def __init__(self) -> None:
        super().__init__()

    def __see(self, data: DataFrame | Series, filtered: Series | None = None):

        if filtered is not None:
            print(data[filtered])
        else:
            print(data)

    def __dropNFirstRows(self, data: DataFrame, n: int):
        return data.iloc[n:]

    def __setIndexInplace(self, data: DataFrame | Series, label: str):
        data.set_index(label, inplace=True)

    def __sortInplace(self, data: DataFrame, column: str | Sequence[str], firstLowers: bool = True, key=None):
        data.sort_values(column, inplace=True, ascending=firstLowers, key=key)

    def __sortByIndexInplace(self, data: DataFrame | Series, firstLowers: bool = True, key=None):
        data.sort_index(inplace=True, ascending=firstLowers, key=key)

    def __plotAndShow(self, data: Series, kind: str = "bar", sortIndex: bool = False):
        myLogger(level="info", msg="ploting...")

        data.sort_index(inplace=True) if sortIndex else ""

        data.plot(kind=kind)
        plt.show()

    def __filterAndReturnCol(self, df: _DFname, mask: Series, col: List[str]) -> DataFrame | Series:

        return self.getDF(df)[mask][col]

    def __reanameCols(
        self,
        df: _DFname,
        mapper: Renamer,
    ) -> None:

        self.getDF(df).rename(columns=mapper, inplace=True)

    def __changeType(self, df: _DFname, col: List[str], newType):

        self.getDF(df)[col] = self.getDF(df)[col].astype(newType)

    def main(self):
        # self.__see(self.apps)
        # logic here
        self.apps.info()



        

