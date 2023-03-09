from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

from icecream import ic

# Create your views here.


class ArtticlesListView(ListView):
    model = Article
    template_name = "articles/articles_list.html"
    context_object_name = "articles"
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    context_object_name = "article"
    succes_url = reverse_lazy("articles:articles_list")
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class

        # if self.request.user.is_authenticated:
        context["comments"] = Comment.objects.filter(article=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            text=request.POST.get("text"),
            author=request.user,
            article=self.get_object(),
        )

        new_comment.save()
        return self.get(request, *args, **kwargs)

class ArticleCreateView(CreateView):
    model = Article
    template_name = "articles/article_from.html"
    success_url = reverse_lazy("articles:articles_list")
    form_class = ArticleForm


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "articles/article_from.html"
    success_url = reverse_lazy("articles:articles_list")
    form_class = ArticleForm


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("articles:articles_list")


class CommentCreateView(CreateView):
    model = Comment
    template_name = "articles/comment_from.html"
    success_url = reverse_lazy("articles:articles_list")
    form_class = CommentForm
