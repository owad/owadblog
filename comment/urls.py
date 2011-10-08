from django.conf.urls.defaults import *
from comment.views import CommentCreateView

urlpatterns = patterns('comment.views',
    url(r'^details/(?P<article_id>\d+)/$', CommentCreateView.as_view(), name='comment_create'),
    
#    url(r'^new$', CaseAddView.as_view(), name='case_add'),
#    url(r'^edit/(?P<pk>\d+)/$', CaseEditView.as_view(), name='case_edit'),
#    url(r'^delete/(?P<pk>\d+)/$', CaseDelView.as_view(), name='case_del'),
)
