from django.db import models

class MyProject(models.Model):
    text = models.TextField(max_length=3000)
    