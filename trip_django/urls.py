# urls.py는 사용자가 어떤 URL형식으로 접근했을 때 어떻게 웹 사이트를 작동시킬지 정리해 놓은 파일
# urls.py는 표지판 역활임.

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# blog/로 접속할 때 blog 폴더의 urls.py를 참조하도록 하는 코드
# URL이 들어올 때 어떻게 처리할 것인지 명시해 주는 코드
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', include('single_pages.urls')),
    path('accounts/',include('allauth.urls')),
]
#미디어 파일을 위한 URL 지정 코드
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)