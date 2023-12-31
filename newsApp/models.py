from django.db import models
from userApp.models import User


class NewsPost(models.Model):
    date_create = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Created date")
    date_update = models.DateTimeField(blank=True, auto_now=True, verbose_name="Updated date")
    title = models.CharField(max_length=255, blank=False, verbose_name="Title")
    text = models.TextField(blank=False, verbose_name="Text")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Author", related_name="newsposts")
    
    def __str__(self):
        return f"{self.title}... © {self.author}"

    def num_likes(self):
        return self.like_set.count()
    
    class Meta:
        ordering = ('-date_create', )
    

class Comment(models.Model):
    newspost = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    date_create = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Created date")
    text = models.TextField(blank=False, verbose_name="Text")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author", related_name="comments")

    def __str__(self):
        return f'{self.text[:10]} - {self.newspost}'
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newspost = models.ForeignKey(NewsPost, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'newspost')