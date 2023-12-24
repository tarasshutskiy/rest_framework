from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Info(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Info'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
