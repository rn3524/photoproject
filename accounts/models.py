from django.db import models
from django.contrib.auth.models import AbstractUser # AbustrectUserクラス)(ユーザテーブルのひな型)インポート

class CustomUser(AbstractUser):
    '''
    用意されているユーザから特に変更しないで使う
    '''
    pass
