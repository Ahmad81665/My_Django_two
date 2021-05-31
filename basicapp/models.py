from django.db import models

# Create your models here.

class form_db(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField()