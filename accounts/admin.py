from django.contrib import admin
from .models import CustomUser # CustomUserをインポート

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username') # レコード一覧にidとusernameを表示
    list_display_links = ('id', 'username') # 表示するカラムにリンクを設定

# django管理サイトにCustomUser、CustomUserAdminを登録する
admin.site.register(CustomUser, CustomUserAdmin)