from django.urls import path, re_path
from .views import (
    TestimonialCreateView,
    TestimonialUpdateView,
    TestimonialDeleteView,
    TestimonialListViews,
    TestimonialRedirectView
)

app_name = "testimonials"

urlpatterns = [
    path("", TestimonialListViews.as_view(), name="testimonials_list"),
    path("create/", TestimonialCreateView.as_view(), name="testimonials_create"),
    path(
        "<int:pk>/update/", TestimonialUpdateView.as_view(), name="testimonials_update"
    ),
    path(
        "<int:pk>/delete/", TestimonialDeleteView.as_view(), name="testimonials_delete"
    ),
    re_path(r'.+',TestimonialRedirectView.as_view(), name='testimonials_redirect'),
]
