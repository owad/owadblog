from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, \
                                    UpdateView, DeleteView
                                    
from article.models import Article
from article.forms import ArticleForm

class ArticleListView(ListView):
    template_name = 'article/list.html'
    model = Article

class ArticleCreateView(CreateView):
    template_name = 'article/form.html'
    form_class = ArticleForm
    success_url = 'comment_create'
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return HttpResponseRedirect(reverse(self.success_url, kwargs={'article_id': object.id}))

class ArticleUpdateView(UpdateView):
    template_name = 'article/form.html'
    form_class = ArticleForm
    success_url = 'comment_create'
    
    def get_object(self, queryset=None):
        print self.kwargs
        return get_object_or_404(Article, pk=self.kwargs['pk'])
    
    def get_success_url(self):
        return reverse(self.success_url, kwargs={'article_id': self.kwargs['pk']})
    
class ArticleDeleteView(DeleteView):
    template_name = 'article/delete.html'
    model = Article
    success_url = 'article_list'
    
    def get_success_url(self):
        return reverse(self.success_url)