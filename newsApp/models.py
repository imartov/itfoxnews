from django.db import models


class NewsPost(models.Model):
    date_create = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Created date")
    date_update = models.DateTimeField(blank=True, auto_now=True, verbose_name="Updated date")
    title = models.CharField(max_length=250, blank=False, verbose_name="Title")
    text = models.TextField(blank=False, verbose_name="Text")
    # author TODO: key to users
    
    def __str__(self):
        return self.title
