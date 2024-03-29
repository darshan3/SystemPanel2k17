from django.db import models


class ArtsAndIdeasGenre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ArtsAndIdeasEvent(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(ArtsAndIdeasGenre,
                              related_name='genres',
                              on_delete=models.CASCADE)
    description = models.TextField()
    subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.name
