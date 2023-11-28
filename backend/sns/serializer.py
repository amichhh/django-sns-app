from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Friend, Good, Group, Message
from django.contrib.auth.models import User


# メッセージ
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('owner', 'group', 'content', 'share_id',
                  'good_count', 'share_count', 'pub_date')


# グループ
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('owner', 'title')


# フレンド
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('owner', 'user', 'group')


# グッド
class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('owner', 'message')


# ユーザー
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
