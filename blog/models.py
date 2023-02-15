from django.db import models
import os
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'


# title필드는 CharField 클래스로 구성, 최대 길이는 30을 넘지 않도록 정함.
# content필드는 문자열의 길이 제한이 없고, created_at은 초 단위 까지 기록할 수 있도록 구성함.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=50, blank=True)
    content = MarkdownxField()

    #파일 업로드 코드
    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%y/%m/%d/', blank=True)

    # 자동으로 작성 시간 저장되도록 구성. (auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #SET_NULL은 사용자 없으면 빈칸으로 만듬

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags=models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}' 
        #{포스트의 pk값}{포스트의 title값}{포스트의 author값}
        #pk는 각 레코드에 대한 고유값(1부터 시작)

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    #파일명 나오게 하는 함수
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    #확장자를 찾아내는 함수
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/1439/d7bd69a23722d433/svg/{self.author.username}.png'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.author}::{self.content}'
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/1439/d7bd69a23722d433/svg/{self.author.username}.png'