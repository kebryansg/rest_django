from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    slug = models.SlugField(max_length=50)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
