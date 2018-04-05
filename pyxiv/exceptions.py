# -*- coding: utf-8 -*-


class PyxivError(Exception):
    """Pixiv Base Exception"""


class PyxivAuthFailed(PyxivError):
    """Authentication Error"""


class PyxivNotAuthenticatedError(PyxivError):
    """Not Authenticated Error"""
