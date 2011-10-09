from django.conf.urls.defaults import *
from comment.views import CommentCreateView

urlpatterns = patterns('comment.views',
    url(r'^details/(?P<article_id>\d+)/$', CommentCreateView.as_view(), name='comment_create'),
)
