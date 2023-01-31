from django.contrib import admin
from .models import Post, Category, Tag,Comment
from markdownx.admin import MarkdownxModelAdmin

# 127.0.0.1/admin 으로 접속하면 Blog에 Posts 관리 가능하게 해주는 코드
admin.site.register(Post,MarkdownxModelAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# 127.0.0.1/admin 으로 접속하면 Blog에 Categorys 관리 가능하게 해주는 코드
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
