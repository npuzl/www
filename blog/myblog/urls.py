from django.urls import path, include
from . import views
import notifications.urls

# 正在部署的应用的名称
app_name = 'myblog'

urlpatterns = [
    path('home/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name='article_safe_delete'
    ),
    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path(
        'increase-likes/<int:id>/',
        views.IncreaseLikesView.as_view(),
        name='increase_likes'
    ),
]
