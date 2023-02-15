# 관리자 페이지에 모델 등록한는 페이지.
# 현재 상태: Post, Category, Tag, Comment 페이지 형성됨.

from django.contrib import admin
from .models import Post, Category, Tag,Comment
from markdownx.admin import MarkdownxModelAdmin

# 카테고리 모델의 name필드에 값이 입력돼면 자동으로 slug가 만들어짐
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# 127.0.0.1/admin 으로 접속하면 Blog에 Categorys 관리 가능하게 해주는 코드
# 127.0.0.1/admin 으로 접속하면 Blog에 Tag 관리 가능하게 해주는 코드
# 127.0.0.1/admin 으로 접속하면 Blog에  Comment 관리 가능하게 해주는 코드
# 127.0.0.1/admin 으로 접속하면 Blog에 Post 관리 가능하게 해주는 코드
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Post,MarkdownxModelAdmin)
