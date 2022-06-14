from typing_extensions import Literal, TypeAlias


__all__ = ["_MyloggingLevel", "_FormatSaveFlie"]

_MyloggingLevel: TypeAlias = Literal["error", "info"]


_FormatSaveFlie: TypeAlias = Literal["to_csv", "to_pickle", "to_sql"]
