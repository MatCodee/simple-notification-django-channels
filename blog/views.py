from django.shortcuts import render
#from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Post,Comment
    
class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['comment'] = Comment.objects.filter(post__id=pk)
        return context


'''
# En caso de especificar un contexto pero es mejor usar esto cuando quieres mostrar una pagina statica
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['blogs'] = Post.objects.all()
        return context
    
class DetailView(TemplateView):
    template_name = 'detail.html'
    
    def get_context_data(self,id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Post.objects.get(id=id)
        return context


# Contexto separado de la clase
class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_additional_context())
        return context

    def get_additional_context(self,pk=None,*args, **kwargs):
        return {}

    
    # En caso de que quieras agregar un contexto permanente para todas las funciones que hereden de este mixin qui esta el codigo
    def get_footer_data(self):
        return {
            'footer_text': 'This is the footer text',
            'footer_links': [
                {'name': 'Link 1', 'url': 'https://example.com/link1'},
                {'name': 'Link 2', 'url': 'https://example.com/link2'},
                {'name': 'Link 3', 'url': 'https://example.com/link3'},
            ]
        }


'''



