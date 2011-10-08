from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    date_add = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title