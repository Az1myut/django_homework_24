from email import message
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from persons.models import PersonAbstract
class ContactInfo(models.Model):
    description = models.CharField(verbose_name = 'Описание', max_length=255, blank=True)
    office = models.CharField(verbose_name='Офис', max_length=150)
    phone = models.CharField(verbose_name='Телефон', max_length= 62)
    email = models.EmailField(verbose_name='Email')
    class Meta:
        verbose_name=_('Контактная информация')
        verbose_name_plural=_('Контактные информации')
    
    def __str__(self)->str:
        return f'{self.office}'
    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('', kwargs={'pk': self.pk})

class ContactMessage(PersonAbstract):
    subject = models.CharField(verbose_name='Тема', max_length=150)
    message = models.TextField(verbose_name='Сообщение', blank=True)

    class Meta:
        verbose_name=_('Сообщение')
        verbose_name_plural=_('Сообщения')
    
    def __str__(self)->str:
        return f'{self.subject}'