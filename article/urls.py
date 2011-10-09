from django.conf.urls.defaults import *
from article.views import ArticleListView, ArticleCreateView, \
                            ArticleDeleteView, ArticleUpdateView
from django.contrib.auth.views import login, login_required

urlpatterns = patterns('article.views',
    url(r'^$', ArticleListView.as_view(), name='article_list'),
    url(r'^article/create', login_required(ArticleCreateView.as_view()), name='article_create'),
    url(r'^article/update/(?P<pk>\d+)/', login_required(ArticleUpdateView.as_view()), name='article_update'),
    url(r'^article/delete/(?P<pk>\d+)/$', login_required(ArticleDeleteView.as_view()), name='article_delete'),
)
