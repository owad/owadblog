from django.db import models
from article.models import Article

class Comment(models.Model):
    
    nickname = models.CharField(max_length=64, blank=False)
    email = models.EmailField(blank=True)
    content = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    
    article = models.ForeignKey(Article)
    
    def __unicode__(self):
        return self.content
