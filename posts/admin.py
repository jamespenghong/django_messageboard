from django.contrib import admin

from .models import Post,Comment

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
# 设置在post里显示comment


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)