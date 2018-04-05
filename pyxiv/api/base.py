# -*- coding: utf-8 -*-


class PixivApiBase(object):

    def __init__(self, oauth, base_url):
        super(PixivApiBase, self).__init__()
        self._oauth = oauth
        self._base_url = base_url
