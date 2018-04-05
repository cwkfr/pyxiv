# -*- coding: utf-8 -*-
from enum import Enum


class ContentType(Enum):
    ILLUST = "illust"
    MANGA = "manga"
    NOVEL = "novel"
    USER = "user"


class Restrict(Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    ALL = "all"


class SearchAspectRatio(Enum):
    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"
    SQUARE = "square"


class SearchIllustTool(Enum):
    PHOTOSHOP = "photoshop"
    ILLUSTRATOR = "illustrator"
    FIREWORKS = "fireworks"


class SearchSize(Enum):
    MINIMUM = "minimum"
    MEDIUM = "medium"
    LARGE = "large"


class SearchSort(Enum):
    DESC = "date_desc"
    ASC = "date_asc"
    POPULAR_DESC = "popular_desc"


class XRestrict(Enum):
    GENERAL = 0
    R18 = 1
    R18G = 2
