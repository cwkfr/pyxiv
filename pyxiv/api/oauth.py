# -*- coding: utf-8 -*-
import requests

from ..exceptions import PyxivError, PyxivAuthFailed
from ..constants import (
    OS, OS_VERSION, VERSION, USER_AGENT, CLIENT_ID, CLIENT_SECRET, OAUTH_URL
)


class OAuth(object):

    def __init__(self, session=None):
        super(OAuth, self).__init__()
        self._session = requests.Session() if session is None else session
        self._session.headers.update({
            'User-Agent': USER_AGENT,
            'App-OS': OS,
            'App-OS-Version': OS_VERSION,
            'App-Version': VERSION,
        })

        self._access_token = None
        self._refresh_token = None

        self._id = None
        self._name = None
        self._username = None
        self._device_token = 'pixiv'

        self.__password = None

    def _req(self, method, url, params=None, data=None, headers=None,
             is_retry=False):
        req = self._session.request(method, url, params, data, headers)

        if req.status_code == 400:
            try:
                r = req.json()
                if r['errors']['system']['code'] == 1508:
                    if is_retry:
                        raise PyxivError(req.text)
                    self._auth()
                    self._req(method, url, params, data, headers, True)
            except (ValueError, KeyError):
                req.raise_for_status()
        elif req.status_code != 200:
            raise PyxivError(req.text)
        else:
            return req.json()

    def _auth(self, username=None, password=None):
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'device_token': self._device_token,
            'get_secure_url': True,
        }

        if username is not None and password is not None:
            self._username = username
            self.__password = password
            data['grant_type'] = 'password'
            data['username'] = username
            data['password'] = password
        else:
            data['grant_type'] = 'refresh_token'

        self._session.headers.pop('Authorization', None)
        url = OAUTH_URL + "/auth/token"
        req = self._session.post(url, data=data)

        if req.status_code != 200:
            try:
                r = req.json()
                if r['errors']['system']['code'] == 1508:
                    raise PyxivAuthFailed(req.text)
            except KeyError:
                raise PyxivAuthFailed(req.text)

        r = req.json()['response']
        self._access_token = r['access_token']
        self._refresh_token = r['refresh_token']
        self._id = r['user']['id']
        self._name = r['user']['name']
        self._username = r['user']['account']
        self._device_token = r['device_token']

        self._session.headers.update({
            'Authorization': 'Bearer ' + self._access_token
        })

    def _login(self, username, password, device_token=None):
        if device_token is not None:
            self.device_token = device_token
        self._auth(username, password)
