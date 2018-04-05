# -*- coding: utf-8 -*-
from .base import PixivApiBase
from ..constants import ACCOUNTS_URL, PROVISIONAL_TOKEN
from ..decorators import POST, Field, Authenticated


class Account(PixivApiBase):

    PROVISIONAL_AUTH = {'Authorization': 'Bearer ' + PROVISIONAL_TOKEN}

    def __init__(self, oauth):
        super(Account, self).__init__(oauth, ACCOUNTS_URL)

    @POST("/api/provisional-accounts/create", headers=PROVISIONAL_AUTH)
    def createProvisionalAccount(self, user_name: Field, ref: Field):
        """Create a temporary account."""

    @Authenticated
    @POST("/api/account/edit")
    def editAccount(self, new_mail_address, new_user_account, current_password,
                    new_password):
        pass
