from django.conf.urls.defaults import *
from article.views import ArticleListView, ArticleCreateView, \
                            ArticleDeleteView, ArticleUpdateView

urlpatterns = patterns('article.views',
    url(r'^$', ArticleListView.as_view(), name='article_list'),
    url(r'^article/create', ArticleCreateView.as_view(), name='article_create'),
    url(r'^article/update/(?P<pk>\d+)/', ArticleUpdateView.as_view(), name='article_update'),
    url(r'^article/delete/(?P<pk>\d+)/$', ArticleDeleteView.as_view(), name='article_delete'),

#    url(r'^new$', CaseAddView.as_view(), name='case_add'),
#    url(r'^edit/(?P<pk>\d+)/$', CaseEditView.as_view(), name='case_edit'),
#    url(r'^delete/(?P<pk>\d+)/$', CaseDelView.as_view(), name='case_del'),
)
