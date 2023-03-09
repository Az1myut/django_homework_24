from django.contrib import admin
from .models import Testimonial
# Register your models here.


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'testimonial', 'created_at', 'updated_at', 'active')
    list_editable = ('active',)
    search_fields = ('title', 'testimonial', 'created_at', 'updated_at')
    list_filter = ('title', 'testimonial', 'created_at', 'updated_at')

admin.site.register(Testimonial, TestimonialAdmin)