#이 페이지의 함수들은 데이터베이스와 연결 필요 없이 단순히 html만 연결시키면 됨.
#render()함수 내에 딕셔너리로 인자를 전달할 필요 없음.
from django.shortcuts import render
from blog.models import Post

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
