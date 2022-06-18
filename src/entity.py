from sqlite3 import connect
from typing import Literal, Any
import pandas as pd
from .types import _FormatSaveFlie, _DFname
from src.utils import myLogger, basePath


class Entity:
    commentsFile = "AppsCommentsLessThan3yEn.pkl"
    appsFile = "Apps.sqlite"

    def __init__(self) -> None:
        myLogger(level="info", msg="reading files...")

        pd.set_option("display.width", 70)

        # self.comments: pd.DataFrame = pd.read_pickle(f"{basePath}/{self.commentsFile}")

        self.apps = pd.read_sql(
            "SELECT * FROM 'Apps.sqlite'",
            con=connect(f"{basePath}/{self.appsFile}"),
            columns=[
                "title",
                "genre",
                "appId",
                "minInstalls",
                "ratings",
                "published_days",
                "daily_installs",
                "daily_ratings",
                "installs_ratings_ratio",
                "summary",
                "developerId",
                "description",
            ],
        )

        # self.apps = pd.read_parquet('./files/parquetExs.gzip')

        # self.apps: pd.DataFrame = pd.read_pickle(f"{basePath}/{'Apps.pkl'}")

        # self.apps: pd.DataFrame = pd.read_parquet(f"{basePath}/{'Apps.gzip'}")
        # self.apps: pd.DataFrame = pd.read_feather(f"{basePath}/{'Apps'}")

        # self.btc: pd.DataFrame = pd.read_csv(f"{basePath}/{self.bitcoinFile}")
        # self.hapiness: pd.DataFrame = pd.read_csv(f"{basePath}/{self.hapinessFile}",index_col=1)

        # self.houses: pd.DataFrame = pd.read_csv(f"{basePath}/{self.housesFile}")

        # self.titanic: pd.DataFrame = pd.read_csv(f"{basePath}/{self.titanicFile}")

    def getDF(self, name: _DFname) -> pd.DataFrame:
        return getattr(self, name)

    def saveCurrentDF(self, name: _DFname, to: _FormatSaveFlie, fileName: str):
        myLogger(level="info", msg="saving file...")

        path = f"{basePath}/{fileName}"

        df = self.getDF(name=name)
        df.info()
        kwargs: dict[str, Any] | Literal[""] = (
            {"index": False, "path_or_buf": path}
            if to == "to_csv"
            else {"path": path}
            if to == "to_pickle"
            else {"name": fileName, "index": False, "if_exists": "replace", "con": connect(path)}
            if to == "to_sql"
            else ""
        )
        getattr(df, to)(**kwargs)

    def saveNewDF(self, data: pd.DataFrame, to: _FormatSaveFlie, name: str):
        myLogger(level="info", msg="saving file...")
        path = f"{basePath}/{name}"

        kwargs: dict[str, Any] | Literal[""] = (
            {"index": False, "path_or_buf": path}
            if to == "to_csv"
            else {"path": path}
            if to == "to_pickle"
            else {"name": name, "index": False, "if_exists": "replace", "con": connect(path)}
            if to == "to_sql"
            else ""
        )
        getattr(data, to)(**kwargs)
