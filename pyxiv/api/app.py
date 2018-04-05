# -*- coding: utf-8 -*-
from .base import PixivApiBase
from ..constants import APP_URL
from ..decorators import GET, POST, Field, Query, Authenticated


class App(PixivApiBase):

    def __init__(self, oauth):
        super(App, self).__init__(oauth, APP_URL)

    @Authenticated
    @POST("/v1/illust/comment/delete")
    def deleteIllustComment(self, comment_id: Field):
        pass

    @Authenticated
    @POST("/v1/novel/comment/delete")
    def deleteNovelComment(self, comment_id: Field):
        pass

    @GET("/v1/application-info/android")
    def getApplicationInfo(self):
        pass

    @GET("/v1/emoji")
    def getEmoji(self):
        pass

    @Authenticated
    @GET("/v2/illust/follow")
    def getFollowIllusts(self, restrict: Query):
        pass

    @Authenticated
    @GET("/v1/novel/follow")
    def getFollowNovels(self, restrict: Query):
        pass

    @Authenticated
    @GET("/v1/user/follow/detail")
    def getFollowUserDetail(self, user_id: Query):
        pass

    @GET("/v1/walkthrough/force-like-illusts")
    def getForceLikeIllusts(self):
        pass

    @Authenticated
    @GET("/v1/illust/detail?filter=for_android")
    def getIllust(self, illust_id: Query):
        pass

    @Authenticated
    @GET("/v1/user/bookmark-tags/illust")
    def getIllustBookmarkTags(self, user_id: Query, restrict: Query):
        pass

    @Authenticated
    @GET("/v1/user/browsing-history/illusts")
    def getIllustBrowsingHistory(self):
        pass

    @Authenticated
    @GET("/v2/illust/comments")
    def getIllustComments(self, illust_id: Query):
        pass

    @Authenticated
    @GET("/v1/illust/ranking?filter=for_android")
    def getIllustRanking(self, mode: Query, date: Query):
        pass

    @Authenticated
    @GET("/v2/illust/related?filter=for_android")
    def getIllustRecommended(self, illust_id: Query):
        pass

    @Authenticated
    @GET("/v1/illust/comment/replies")
    def getIllustReplyComments(self, comment_id: Query):
        pass

    @Authenticated
    @GET("/v1/illust-series/illust?filter=for_android")
    def getIllustSeriesByIllustId(self, illust_id: Query):
        pass

    @Authenticated
    @GET("/v1/illust/series?filter=for_android")
    def getIllustSeriesDetailsBySeriesId(self, illust_series_id: Query):
        pass

    @Authenticated
    @GET("/v1/trending-tags/illust?filter=for_android")
    def getIllustTrendTags(self):
        pass

    @Authenticated
    @GET("/v1/user/bookmarks/illust")
    def getLikeIllust(self, user_id: Query, restrict: Query, tag: Query):
        pass

    @Authenticated
    @GET("/v2/illust/bookmark/detail")
    def getLikeIllustDetail(self, illust_id: Query):
        pass

    @Authenticated
    @GET("/v1/user/bookmarks/novel")
    def getLikeNovel(self, user_id: Query, restrict: Query, tag: Query):
        pass

    @Authenticated
    @GET("/v2/novel/bookmark/detail")
    def getLikeNovelDetail(self, novel_id: Query):
        pass

    @Authenticated
    @GET("/v1/illust/bookmark/users?filter=for_android")
    def getLikedIllustUser(self, illust_id: Query):
        pass

    @Authenticated
    @GET("/v1/novel/bookmark/users")
    def getLikedNovelUser(self, novel_id: Query):
        pass

    @Authenticated
    @GET("v1/live/list")
    def getLiveList(self, list_type: Query):
        pass

    @Authenticated
    @POST("v1/mail-authentication/send")
    def getMailAuthentication(self):
        pass

    @Authenticated
    @GET("/v1/mute/list")
    def getMutedList(self):
        pass

    @Authenticated
    @GET("/v2/illust/mypixiv")
    def getMyPixivIllusts(self):
        pass

    @Authenticated
    @GET("/v1/novel/mypixiv")
    def getMyPixivNovels(self):
        pass

    @Authenticated
    @GET("/v1/notification/new-from-following")
    def getNewFromFollowingNotification(self, latest_seen_illust_id: Query,
                                        latest_seen_novel_id: Query,
                                        last_notified_datetime: Query):
        pass

    @Authenticated
    @GET("/v1/illust/new?filter=for_android")
    def getNewIllust(self, content_type: Query):
        pass

    @Authenticated
    @GET("/v1/novel/new")
    def getNewNovel(self):
        pass

    @Authenticated
    @GET("/v1/notification/settings")
    def getNotificationSettings(self):
        pass

    @Authenticated
    @GET("/v2/novel/detail")
    def getNovel(self, novel_id: Query):
        pass

    @Authenticated
    @GET("v1/user/bookmark-tags/novel")
    def getNovelBookmarkTags(self, user_id: Query, restrict: Query):
        pass

    @Authenticated
    @GET("/v1/user/browsing-history/novels")
    def getNovelBrowsingHistory(self):
        pass

    @Authenticated
    @GET("/v2/novel/comments")
    def getNovelComments(self, novel_id: Query):
        pass

    @Authenticated
    @GET("v2/novel/markers")
    def getNovelMarkers(self):
        pass

    @Authenticated
    @GET("/v1/novel/ranking")
    def getNovelRanking(self, mode: Query, date: Query):
        pass

    @Authenticated
    @GET("/v1/novel/comment/replies")
    def getNovelReplyComments(self, comment_id: Query):
        pass

    @Authenticated
    @GET("/v1/novel/series")
    def getNovelSeries(self, series_id: Query):
        pass

    @Authenticated
    @GET("/v1/novel/text")
    def getNovelText(self, novel_id: Query):
        pass

    @Authenticated
    @GET("/v1/trending-tags/novel")
    def getNovelTrendTags(self):
        pass

    @Authenticated
    @GET("/v1/spotlight/articles?filter=for_android")
    def getPixivisionArticles(self, category: Query):
        pass

    @Authenticated
    @GET("/v1/search/popular-preview/illust?filter=for_android")
    def getPopularPreviewIllust(self, word: Query, search_target: Query,
                                start_date: Query, end_date: Query):
        pass

    @Authenticated
    @GET("/v1/search/popular-preview/novel")
    def getPopularPreviewNovel(self, word: Query, search_target: Query,
                               start_date: Query, end_date: Query):
        pass

    @GET("/v1/user/profile/presets")
    def getProfilePresets(self):
        pass

    @Authenticated
    @GET("/v1/illust/recommended?filter=for_android")
    def getRecommendedIllusts(self, include_ranking_illusts: Query):
        pass

    @Authenticated
    @GET("/v1/manga/recommended?filter=for_android")
    def getRecommendedMangaList(self, include_ranking_illusts: Query,
                                bookmark_illust_ids: Query):
        pass

    @Authenticated
    @GET("/v1/novel/recommended")
    def getRecommendedNovels(self, include_ranking_novels: Query):
        pass

    @Authenticated
    @GET("/v1/search/autocomplete")
    def getSearchAutoCompleteKeywords(self, word: Query):
        pass

    @Authenticated
    @GET("/v1/search/illust?filter=for_android")
    def getSearchIllust(self, word: Query, sort: Query, search_target: Query,
                        bookmark_num_min: Query, bookmark_num_max: Query,
                        start_date: Query, end_date: Query):
        pass

    @Authenticated
    @GET("/v1/search/bookmark-ranges/illust?filter=for_android")
    def getSearchIllustBookmarkRanges(self, word: Query, search_target: Query,
                                      start_date: Query, end_date: Query):
        pass

    @Authenticated
    @GET("/v1/search/novel")
    def getSearchNovel(self, word: Query, sort: Query, search_target: Query,
                       bookmark_num_min: Query, bookmark_num_max: Query,
                       start_date: Query, end_date: Query):
        pass

    @Authenticated
    @GET("/v1/search/bookmark-ranges/novel")
    def getSearchNovelBookmarkRanges(self, word: Query, search_target: Query,
                                     start_date: Query, end_date: Query):
        pass

    @Authenticated
    @GET("/v1/search/user?filter=for_android")
    def getSearchUser(self, word: Query):
        pass

    @Authenticated
    @GET("v1/ugoira/metadata")
    def getUgoiraMetadata(self, illust_id: Query):
        pass

    @Authenticated
    @POST("v1/upload/status")
    def getUploadIllustStatus(self, convert_key: Field):
        pass

    @Authenticated
    @GET("/v1/user/detail?filter=for_android")
    def getUser(self, user_id: Query):
        pass

    @Authenticated
    @GET("/v1/user/follower?filter=for_android")
    def getUserFollower(self, user_id: Query):
        pass

    @Authenticated
    @GET("/v1/user/following?filter=for_android")
    def getUserFollowing(self, user_id: Query, restrict: Query):
        pass

    @Authenticated
    @GET("/v1/user/illust-series")
    def getUserIllustSeries(self, user_id: Query):
        pass

    @Authenticated
    @GET("/v1/user/illusts?filter=for_android")
    def getUserIllusts(self, user_id: Query, type: Query):
        pass

    @Authenticated
    @GET("/v1/user/me/state")
    def getUserMeState(self):
        pass

    @Authenticated
    @GET("/v1/user/mypixiv?filter=for_android")
    def getUserMyPixiv(self, user_id: Query):
        pass

    @Authenticated
    @GET("/v1/user/novels")
    def getUserNovels(self, user_id: Query):
        pass

    @Authenticated
    @GET("/v1/user/recommended?filter=for_android")
    def getUserRecommended(self):
        pass

    @Authenticated
    @GET("/v1/user/related?filter=for_android")
    def getUserRelated(self, seed_user_id: Query):
        pass

    @GET("v1/walkthrough/illusts")
    def getWalkthroughIllusts(self):
        pass

    @Authenticated
    @POST("/v2/user/browsing-history/illust/add")
    def postAddIllustBrowsingHistory(self, illust_ids: Field):
        pass

    @Authenticated
    @POST("/v2/user/browsing-history/novel/add")
    def postAddNovelBrowsingHistory(self, novel_ids: Field):
        pass

    @Authenticated
    @POST("v1/novel/marker/add")
    def postAddNovelMarker(self, novel_id: Field, page: Field):
        pass

    @Authenticated
    @POST("/v1/dev/ios/receipt/post")
    def postDebugReceipt(self, receipt_data: Field):
        pass

    @Authenticated
    @POST("/v1/illust/delete")
    def postDeleteIllust(self, illust_id: Field):
        pass

    @Authenticated
    @POST("/v1/novel/delete")
    def postDeleteNovel(self, novel_id: Field):
        pass

    @Authenticated
    @POST("v1/novel/marker/delete")
    def postDeleteNovelMarker(self, novel_id: Field):
        pass

    @Authenticated
    @POST("/v1/notification/settings/edit")
    def postEditNotificationSettings(self, enabled_notification_types: Field):
        pass

    @Authenticated
    @POST("/v1/feedback")
    def postFeedback(self, message: Field, device: Field, dimension01: Field,
                     dimension02: Field, dimension03: Field, dimension04: Field):
        pass

    @Authenticated
    @POST("/v1/user/follow/add")
    def postFollowUser(self, user_id: Field, restrict: Field):
        pass

    @Authenticated
    @POST("/v1/illust/comment/add")
    def postIllustComment(self, illust_id: Field, comment: Field,
                          parent_comment_id: Field):
        pass

    @Authenticated
    @POST("/v2/illust/bookmark/add")
    def postLikeIllust(self, illust_id: Field, restrict: Field, tags: Field):
        pass

    @Authenticated
    @POST("/v2/novel/bookmark/add")
    def postLikeNovel(self, novel_id: Field, restrict: Field, tags: Field):
        pass

    @Authenticated
    @POST("/v1/mute/edit")
    def postMuteSetting(self, add_user_ids: Field, delete_user_ids: Field,
                        add_tags: Field, delete_tags: Field):
        pass

    @Authenticated
    @POST("v1/novel/comment/add")
    def postNovelComment(self, novel_id: Field, comment: Field,
                         parent_comment_id: Field):
        pass

    @Authenticated
    @POST("v1/notification/user/register")
    def postRegisterForNotifications(self, timezone_offset: Field,
                                     disable_notifications: Field):
        pass

    @Authenticated
    @POST("/v1/premium/android/register")
    def postRegisterPremium(self, purchase_data: Field, signature: Field,
                            app_version: Field):
        pass

    @Authenticated
    @POST("/v1/user/follow/delete")
    def postUnfollowUser(self, user_id: Field):
        pass

    @Authenticated
    @POST("/v1/illust/bookmark/delete")
    def postUnlikeIllust(self, illust_id: Field):
        pass

    @Authenticated
    @POST("/v1/novel/bookmark/delete")
    def postUnlikeNovel(self, novel_id: Field):
        pass

    # @Authenticated
    # @POST("v1/upload/illust")
    # def postUploadIllust(self, requestBody):
    #     pass

    # @Authenticated
    # @POST("/v1/user/profile/edit")
    # def postUserProfileEdit(self, requestBody):
    #     pass

    @Authenticated
    @POST("/v1/user/workspace/edit")
    def postUserWorkspaceEdit(self, pc: Field, monitor: Field, tool: Field,
                              scanner: Field, tablet: Field, mouse: Field,
                              printer: Field, desktop: Field, music: Field,
                              desk: Field, chair: Field, comment: Field):
        pass
