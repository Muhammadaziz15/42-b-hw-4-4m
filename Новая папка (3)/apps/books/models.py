from django.db import models


class Book(models.Model):
    title = models.CharField('Название книги', max_length=200)
    author = models.CharField('Автор', max_length=100)
    year = models.IntegerField('Год издания')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
