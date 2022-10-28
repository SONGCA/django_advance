from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Article(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, db_column='userkey')
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)