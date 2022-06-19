from typing_extensions import Literal, TypeAlias, OrderedDict
from typing import List, Dict


__all__ = ["_MyloggingLevel", "_FormatSaveFlie", "_DFname", "_Genres", "_KwsSearch"]

_MyloggingLevel: TypeAlias = Literal["error", "info"]


_FormatSaveFlie: TypeAlias = Literal["to_csv", "to_pickle", "to_sql"]

_DFname: TypeAlias = Literal["apps", "comments", "titanic"]

_Genres: TypeAlias = Literal[
    "Adventure",
    "Arcade",
    "Art & Design",
    "Auto & Vehicles",
    "Beauty",
    "Board",
    "Books & Reference",
    "Business",
    "Casino",
    "Casual",
    "Communication",
    "Dating",
    "Education",
    "Entertainment",
    "Events",
    "Fice",
    "Food & Drink",
    "Health & Fitness",
    "House & Home",
    "Lifestyle",
    "Maps & Navigation",
    "Medical",
    "Music & Audio",
    "News & Magazines",
    "Personalization",
    "Photography",
    "Productivity",
    "Puzzle",
    "Racing",
    "RolePlaying",
    "Social",
    "Sports",
    "Strategy",
    "Tools",
    "Travel & Local",
    "Trivia",
    "VideoPlayers&Editors",
    "Word",
]

_KwsSearch:TypeAlias = Dict[Literal['description','summary','title'],str]

