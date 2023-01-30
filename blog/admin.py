from django.contrib import admin
from .models import Post, Category


#127.0.0.1/admin 으로 접속하면 Blog에 Posts 관리 가능하게 해주는 코드
admin.site.register(Post)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

#127.0.0.1/admin 으로 접속하면 Blog에 Categorys 관리 가능하게 해주는 코드
admin.site.register(Category, CategoryAdmin)