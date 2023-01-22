from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Comment)
class NameAdmin(admin.ModelAdmin):
    list_display = ('name','body', 'post', 'active', 'created_on')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)