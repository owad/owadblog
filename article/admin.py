from django.contrib import admin
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    
admin.site.register(Article, ArticleAdmin)