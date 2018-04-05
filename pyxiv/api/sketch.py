# -*- coding: utf-8 -*-
from .base import PixivApiBase
from ..constants import SKETCH_URL
from ..decorators import GET, POST, Field, Path, Authenticated


class Sketch(PixivApiBase):

    def __init__(self, oauth):
        super(Sketch, self).__init__(oauth, SKETCH_URL)

    @GET("/api/lives/{live_uid}.json")
    def getLive(self, live_uid: Path):
        pass

    @GET("/api/lives/{live_uid}/chats.json")
    def getLiveChats(self, live_uid: Path):
        pass

    @Authenticated
    @POST("/api/lives/{live_uid}/hearts.json")
    def postHeart(self, live_uid: Path, count: Field, is_first: Field):
        pass

    @Authenticated
    @POST("/api/lives/{live_uid}/chats.json")
    def postLiveChats(self, live_uid: Path, message: Field):
        pass

    @Authenticated
    @POST("/api/lives/{live_uid}/members.json")
    def postLiveMembers(self, live_uid: Path):
        pass
