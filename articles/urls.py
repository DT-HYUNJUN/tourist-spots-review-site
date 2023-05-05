from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/likes/', views.likes, name='likes'),
    path('<int:article_pk>/bookmark/', views.bookmark, name='bookmark'),
    path('<int:article_pk>/comments/<int:comment_pk>/likes/', views.comment_likes, name='comment_likes'),
    path('<int:article_pk>/comments/<int:comment_pk>/dislikes/', views.comment_dislikes, name='comment_dislikes'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('search/', views.search, name='search'),
    # 태그 목록을 볼 수 있는 url 
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    # 태그가 달린 객체들의 목록
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # path('<int:article_pk>/comments/<int:comment_pk>/update/', views.replyUpdate, name='replyUpdate'),
]
