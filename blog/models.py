from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.title