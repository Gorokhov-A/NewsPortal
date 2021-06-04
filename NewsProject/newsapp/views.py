from django.urls import path
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import  Post, Category
from django.core.paginator import Paginator

class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 10
    # form_class = PostForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class PostDetail(DetailView):
    template_name = 'post.html'
    queryset = Post.objects.all()


def index(request):
    return render(request, 'index.html')