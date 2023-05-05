from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('region/<region_name>', views.region, name='region'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/likes/', views.post_likes, name='post_likes'),
    path('<int:post_pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:post_pk>/comment/<int:comment_pk>/likes/', views.comment_likes, name='comment_likes'),
    
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    # 태그가 달린 객체들의 목록
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]
