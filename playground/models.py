
# models.py
from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)


# Create your models here.
