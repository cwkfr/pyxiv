# -*- coding: utf-8 -*-
from functools import partial as functools_partial, wraps
from inspect import getfullargspec

from uritemplate import URITemplate
from decorator import decorate

from .exceptions import PyxivNotAuthenticatedError


class Field:
    """Request body field"""


class Path:
    """URITemplate parameter"""


class Query:
    """URL query parameter"""


def Authenticated(func):
    def wrapper(f, *args, **kwargs):
        if 'Authorization' not in args[0]._oauth._session.headers:
            raise PyxivNotAuthenticatedError('You are not logged in!')
        return func(*args, **kwargs)
    return decorate(func, wrapper)


def Request(method, path, returns=None, **option):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(f, *args, **kwargs):
            argspec = getfullargspec(func)
            uri = URITemplate(path)
            field, path_, query = {}, {}, {}

            # Parse each args and put them in the right place
            for n, (key, val) in enumerate(argspec.annotations.items(), 1):
                if val is Field:
                    field[key] = args[n]
                elif val is Path:
                    path_[key] = args[n]
                elif val is Query:
                    query[key] = args[n]

            option['data'] = field
            option['params'] = query

            url = args[0]._base_url + str(uri.partial(path_))
            result = args[0]._oauth._req(method, url, **option)
            if returns is None:
                return result
            return returns(result)
        return decorate(func, inner_wrapper)
    return wrapper


GET = functools_partial(Request, 'GET')
POST = functools_partial(Request, 'POST')
