from django.forms import ModelForm
from article.models import Article
from tinymce.widgets import TinyMCE

class ArticleForm(ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user',)
        widgets = {
           'content': TinyMCE(attrs={
                'cols': 80, 
                'rows': 20
            }, 
            mce_attrs={
               'language': 'en',
               'theme': 'advanced'
           })}

