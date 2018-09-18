from django.contrib import admin

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'status', 'author', 'created', 'updated')
    list_filter = ('status',)
    search_fields = ('title', 'body')


admin.site.register(Post, PostAdmin)
