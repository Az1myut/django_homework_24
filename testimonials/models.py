from django.db import models
from persons.models import PersonAbstract

from site_searches.managers import SearchManagerTestimonials

# Create your models here.


class Testimonial(PersonAbstract):
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    testimonial = models.TextField(verbose_name="Отзыв")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    active = models.BooleanField(verbose_name="Активен", default=False)

    objects = SearchManagerTestimonials()

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["first_name", "last_name"]

    def __str__(self) -> str:
        return f"{self.title}"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("testimonials:testimonials_list")
