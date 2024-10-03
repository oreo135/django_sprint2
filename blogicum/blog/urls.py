from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.posts_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
