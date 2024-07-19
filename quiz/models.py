from django.db import models

# Create your models here.
class Quiz(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.CharField(max_length=120)
    question = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    option = models.TextField(default=[])
    correct = models.BooleanField()
    comment_answer = models.TextField(default="")

    