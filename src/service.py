from tkinter import S

from numpy import Infinity
from src.utils import myLogger
from .entity import Entity
from pandas import DataFrame, Series
from pandas._typing import Renamer, Scalar
import matplotlib.pyplot as plt
from typing import Sequence, List
from .types import _DFname, _Genres, _KwsSearch


class Service(Entity):
    def __init__(self) -> None:
        super().__init__()

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

    def __filterAndReturnDf(self, df: _DFname, mask: Series) -> DataFrame:

        return self.getDF(df)[mask]

    def __reanameCols(
        self,
        df: _DFname,
        mapper: Renamer,
    ) -> None:

        self.getDF(df).rename(columns=mapper, inplace=True)

    def __changeType(self, df: _DFname, col: List[str], newType):

        self.getDF(df)[col] = self.getDF(df)[col].astype(newType)

    def __get_apps_per_kw_And_genre(
        self,
        df: _DFname,
        genre: _Genres,
        kws: _KwsSearch,
        maxAge: int = 0,
        minInstalls: int = 0,
        minDailyInstall: int = 0,
        maxInstalls: float = float("inf"),
    ):

        apps_by_category = self.getDF(df).groupby(by="genre").get_group(genre)
        self.syncDF(df, apps_by_category)

        if maxAge | minInstalls | minDailyInstall | bool(maxInstalls):
            if maxAge & minInstalls & minDailyInstall & bool(maxInstalls):
                apps_by_category = self.__filterAndReturnDf(
                    df,
                    (apps_by_category["published_days"] < maxAge)
                    & (apps_by_category["minInstalls"].between(minInstalls, maxInstalls))
                    & (apps_by_category["daily_installs"] >= minDailyInstall),
                )
            elif maxAge:
                apps_by_category = self.__filterAndReturnDf(df, (apps_by_category["published_days"].between(0, maxAge)))

            elif minInstalls:
                apps_by_category = self.__filterAndReturnDf(
                    df, (apps_by_category["minInstalls"].between(maxInstalls, maxInstalls))
                )

            elif minDailyInstall:
                apps_by_category = self.__filterAndReturnDf(
                    df, (apps_by_category["daily_installs"].between(minDailyInstall, float("inf")))
                )

        self.syncDF(df, apps_by_category)

        mask_title = apps_by_category["title"].str.contains(kws["title"], na=False, regex=True, case=False)
        mask_summary = apps_by_category["summary"].str.contains(kws["summary"], na=False, regex=True, case=False)

        totalMask = mask_title & mask_summary

        myLogger(level="info", msg=f"find {totalMask.sum()} apps with given conditions")

        return totalMask

    def __get_info_daily_installs_per_kw_And_genre(
        self, df: _DFname, genre: _Genres, kws: _KwsSearch, maxAge: int = 0, minDailyInstall: int = 0
    ):

        apps = self.__get_apps_per_kw_And_genre(df, genre, kws, maxAge)

        daily_installs = apps if (minDailyInstall) else self.__filterAndReturnCol(df, apps, col=["daily_installs"])

        print(daily_installs.mean() if (minDailyInstall) else daily_installs.describe())

    def __get_info_min_installs_per_kw_And_genre(self, df: _DFname, genre: _Genres, kws: _KwsSearch, maxAge: int = 0):

        apps = self.__get_apps_per_kw_And_genre(df, genre, kws, maxAge)

        min_installs = self.__filterAndReturnCol(df, apps, col=["minInstalls"])

        print(min_installs.describe())

    def __get_info_installs_ratings_ratio(
        self, df: _DFname, genre: _Genres, kws: _KwsSearch, maxAge: int = 0, minInstalls: int = 0
    ):

        apps = self.__get_apps_per_kw_And_genre(df, genre, kws, maxAge, minInstalls)

        ratios = self.__filterAndReturnCol(df, apps, col=["installs_ratings_ratio"])

        print(ratios.describe())

    def __get_total_installs(
        self,
        df: _DFname,
        genre: _Genres,
        kws: _KwsSearch,
    ):
        apps = self.__get_apps_per_kw_And_genre(df, genre, kws)

        daily = self.__filterAndReturnDf(df, apps)["daily_installs"]
        age = self.__filterAndReturnDf(df, apps)["published_days"]

        daily_And_age = daily * age

        print(daily_And_age.sum())

    def main(self):
        # self.__see(self.apps)
        # logic here
        # self.apps.info()
        mask = self.__get_apps_per_kw_And_genre(
            df="apps",
            genre="Tools",
            kws={"title": r"\bqr|\bbarcode", "summary": r"\bscanner|\breader|\bqr"},
        )
        sum = self.__filterAndReturnCol('apps',mask,col=['minInstalls']).sum()

        print(sum)

