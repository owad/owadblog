from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, \
                                    UpdateView, DeleteView
                                    
from comment.forms import CommentForm
from article.models import Article
                                    
class CommentCreateView(CreateView):
    template_name = 'comment/form.html'
    form_class = CommentForm
    success_url = 'comment_create'

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['article'] = get_object_or_404(Article, pk=self.kwargs['article_id'])
        return context
    
    def get_success_url(self):
        return reverse(self.success_url, kwargs={'article_id': self.kwargs['article_id']})

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        article = self.get_context_data()['article']
        new_comment.article = article
        new_comment.save()
        return HttpResponseRedirect(reverse(self.success_url, kwargs={'article_id': article.id}))