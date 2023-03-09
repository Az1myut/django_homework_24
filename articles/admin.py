from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at', 'updated_at', 'title', 'text', 'author', 'slug', 'image')
    list_filter = ('created_at', 'updated_at')
    list_editable = ('title', 'text', 'slug', 'author')
    list_display_links = ('pk', 'created_at', 'updated_at')
    search_fields = ('title', 'text', 'author')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at', 'updated_at', 'text', 'author', 'article')
    list_filter = ('created_at', 'updated_at')
    list_editable = ('text', 'author')
    list_display_links = ('pk', 'created_at', 'updated_at')
    search_fields = ('text', 'author')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
