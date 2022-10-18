from django.urls import path
from blog_content.views import PostCategory, PostIndex, PostSearch, PostDetail

app_name = 'blog_content'

urlpatterns = [
    path('', PostIndex.as_view(), name='index'),
    path('details/<str:slug>/<int:pk>/',
         PostDetail.as_view(), name='detail'),
    path('category/<str:category_slug>/',
         PostCategory.as_view(), name='category'),
    path('search/', PostSearch.as_view(), name='search'),
]
