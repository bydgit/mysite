from django.db import models

class AuthorInfo(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        db_table='authorInfo'

class BookInfo(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(AuthorInfo)
    class Meta:
        db_table="bookInfo"