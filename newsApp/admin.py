from django.contrib import admin
from . import models


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author", "date_create", "date_update")


admin.site.register(models.NewsPost, NewsPostAdmin)
