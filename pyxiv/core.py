# -*- coding: utf-8 -*-
from .api import Account, App, OAuth, Sketch


class Pyxiv(object):
    """Pixiv private API wrapper."""

    def __init__(self, session=None):
        super(Pyxiv, self).__init__()
        self._oauth = OAuth(session)
        self.account = Account(self._oauth)
        self.app = App(self._oauth)
        self.sketch = Sketch(self._oauth)

    def __getattr__(self, name):
        for api in {self.account, self.app, self.sketch}:
            try:
                return getattr(api, name)
            except AttributeError:
                pass
        raise AttributeError(f"{__name__} object has no attribute {name}")

    def login(self, username, password, provisional=False, device_token=None):
        if provisional:
            account = self.account.createProvisionalAccount(
                'Pyxiv', 'pixiv_android_app_provisional_account')
            self._oauth._login(account)
            return

        self._oauth._login(username, password, device_token)
