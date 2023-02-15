from django.urls import path
from . import views #현재 폴더에 있는 views.py를 사용할 수 있게 가져오라는 의미

urlpatterns = [
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('<int:pk>/new_comment/', views.new_comment), #<int:pk>는 정수 형태의 값을 pk라는 변수로 담아 single_post_page()로 넘기라는 의미
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('search/<str:q>/', views.PostSearch.as_view()),
]

