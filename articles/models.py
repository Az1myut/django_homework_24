from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from site_searches.managers import SearchManagerArticles, SearchManagerComments


class Article(models.Model):
    author = models.ForeignKey(
        verbose_name="Автор", to="auth.User", on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name="Заголовок", max_length=256)
    slug = models.SlugField(verbose_name="slug")
    text = models.TextField(verbose_name="Содержание")
    image = models.ImageField(verbose_name="Изображение", upload_to="articles/")
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Изменено", auto_now=True)

    objects = SearchManagerArticles()

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(_(self.title))
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("articles:article_detail", kwargs={"pk": self.pk})

# Comment
class Comment(models.Model):
    article = models.ForeignKey(
        verbose_name="Статья", to="articles.Article", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        verbose_name="Автор",
        to="auth.User",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Изменено", auto_now=True)

    objects = SearchManagerComments()

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self) -> str:
        return f"{self.author.username} - {self.article[:40]}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("articles:article_detail", kwargs={"pk": self.article.pk})