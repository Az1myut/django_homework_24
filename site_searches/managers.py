from django.db import models
from django.db.models import Q

from icecream import ic


class SearchManagerArticles(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()

        if query:
            or_lookup = Q(title__icontains=query) | Q(text__icontains=query)

            qs = qs.filter(or_lookup)

        return qs


class SearchManagerTestimonials(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()

        if query:
            or_lookup = Q(title__icontains=query) | Q(testimonial__icontains=query)
            qs = qs.filter(or_lookup)

        return qs


class SearchManagerComments(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(text__icontains=query))
            qs = qs.filter(or_lookup)


        return qs
