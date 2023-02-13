from csv import list_dialects
from pyclbr import Class
from django.contrib import admin
from .models import ContactInfo, ContactMessage
# Register your models here.

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ( 'description', 'office', 'phone', 'email')
    list_display_links = ('office',)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message')
    list_display_links = ('subject', 'message')

admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)