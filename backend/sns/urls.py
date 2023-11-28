from django.urls import path, include
from rest_framework import routers

from .views import FindMessageApiView, FindMyGroupApiView, FriendViewSet, GetFriendApiView, GetUserApiView, GroupViewSet, MessageViewSet, PostMessageApiView, UserViewSet

# ---REST API---

# DefaultRouter クラスのインスタンスを代入
router = routers.DefaultRouter()
# Group/ にViewSetをルーティングする
router.register('messages', MessageViewSet)
router.register('groups', GroupViewSet)
router.register('friends', FriendViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('message/', FindMessageApiView.as_view(), name='findmessage'),
    path('post/', PostMessageApiView.as_view(), name='post'),
    path('friend/', GetFriendApiView.as_view(), name='friend'),
    path('user/', GetUserApiView.as_view(), name='user'),
    path('mygroup/', FindMyGroupApiView.as_view(), name='mygroup')
]

# ---MVC---

# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('groups', views.groups, name='groups'),
#     path('add', views.add, name='add'),
#     path('creategroup', views.creategroup, name='creategroup'),
#     path('post', views.post, name='post'),
#     path('share/<int:share_id>', views.share, name='share'),
#     path('good/<int:good_id>', views.good, name='good'),
# ]
