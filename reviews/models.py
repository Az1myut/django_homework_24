from django.db import models
from students.models import Student
# Create your models here.

class Review(models.Model):
    comment = models.TextField(verbose_name = 'Отзыв', blank = True)
    student = models.OneToOneField(to = Student , on_delete = models.CASCADE, 
    blank = True,
                                                        related_name = 'review_student')
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-student']
