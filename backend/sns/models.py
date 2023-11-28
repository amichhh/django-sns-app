from django.db import models
from django.contrib.auth.models import User


# Messageクラス
class Message(models.Model):
    # on_delete=models.CASCADE: ForeinKey等で外部テーブルとモデルを紐づける際、参照されたモデルを削除すると関連するモデルも全て削除する
    # 投稿者
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='message_owner')
    # メッセージが投稿されたグループのID
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    # メッセージの内容
    content = models.TextField(max_length=1000)
    # (メッセージをシェアした場合)シェアしたメッセージのID
    share_id = models.IntegerField(default=-1)
    # Goodの数
    good_count = models.IntegerField(default=0)
    # シェアされた数
    share_count = models.IntegerField(default=0)
    # 投稿日時
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'

    def get_share(self):
        return Message.objects.get(id=self.share_id)

    class Meta:
        ordering = ('-pub_date',)


# Groupクラス
class Group(models.Model):
    # グループの作成者
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # グループ名
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Friendクラス
class Friend(models.Model):
    # フレンド所有者のユーザー情報
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend_owner')
    # フレンドのユーザー情報
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' (group: "' + str(self.group) + '")'


# Goodクラス
class Good(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.message) + '" (by' + str(self.owner) + ')'
