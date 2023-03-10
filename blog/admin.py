from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body', 'post', 'active', 'created_on')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','created', 'publish', 'status')
    list_filter= ('created', 'status', 'publish', 'author')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status', 'publish']
    date_hierarchy = 'publish'
