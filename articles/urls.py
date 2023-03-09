from django.urls import path
from .views import ArtticlesListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, CommentCreateView

app_name = 'articles'

urlpatterns = [
    path('', ArtticlesListView.as_view(), name='articles_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]