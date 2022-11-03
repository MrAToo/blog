from django.shortcuts import render, get_object_or_404
from django.views.generic import ( 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)    
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer

from .models import *


class PostListView(ListView):
    '''Список постов'''
    model = Post
    context_object_name = 'posts'
    template_name = 'my_blog/home.html'
    ordering = ['-data_posted']
    paginate_by = 5


class UserPostListView(ListView):
    '''Список постов конкретного пользователя'''
    model = Post
    context_object_name = 'posts'
    template_name = 'my_blog/user_posts.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-data_posted')


class PostDetailView(DetailView):
    '''Информация об одном посте'''
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    '''Создание нового поста'''
    model = Post
    template_name = 'my_blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        '''Делает пользователя автоматически автором поста который он создает'''
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    '''Изменение существующего поста'''
    model = Post
    template_name = 'my_blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        '''Делает пользователя автоматически автором поста который он изменяет'''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''Проверка на то, что является ли автором тот кто хочет изменить пост'''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False         


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''Удаление поста'''
    model = Post
    success_url = '/'

    def test_func(self):
        '''Проверка на то, что является ли автором тот кто хочет удалить пост'''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False         


def about(request):
    return render(request, 'my_blog/about.html', {'title': 'About'})


'''API'''


class PostViewSet(viewsets.ModelViewSet):
    '''CRUD'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        '''возвращает список определенных постов'''
        pk = self.kwargs.get('pk')
        if not pk:
            return Post.objects.all()[:3]

        return Post.objects.filter(pk=pk)


    @action(methods=['get'], detail=True)
    def author(self, request, pk=None):
        '''создаёт новый url по названию функции'''
        authors = User.objects.get(pk=pk)
        return Response({'authors': authors.username})
