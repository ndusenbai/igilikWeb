from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *


class HomeView(ListView):
    model = Post
    context_object_name = "data"
    template_name = 'templatesCreate/home.html'

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').filter(singleType=1)[:3]
        return queryset


class NewsView(ListView):
    model = Post
    template_name = 'templatesCreate/news.html'
    paginate_by = 4
    ordering = ['-time_create']

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').filter(singleType=1)
        return queryset


class SingleNewsView(DetailView):
    model = Post
    template_name = 'templatesCreate/single_news.html'
    pk_url_kwarg = 'pk'
    ordering = ['-id']
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['data'] = Post.objects.filter(~Q(id=(self.kwargs.get('pk')))).order_by('-id')[:2]
        return context


class BlogView(ListView):
    model = Post
    context_object_name = "data"
    template_name = 'templatesCreate/blog.html'
    paginate_by = 4
    ordering = ['-time_create']

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').filter(singleType=2)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(~Q(id=(self.kwargs.get('pk')))).order_by('-id')[:2]
        return context


class SingleBlogView(generic.TemplateView):
    template_name = 'templatesCreate/single_blog.html'


class MyBlogView(ListView):
    model = Post
    context_object_name = "data"
    template_name = 'templatesCreate/my_blog.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').filter(user = self.request.user.id)
        return queryset

class ContactView(generic.TemplateView):
    template_name = 'templatesCreate/Contact.html'

class ProfileView(generic.TemplateView):
    template_name = 'registration/profile.html'

class AboutView(generic.TemplateView):
    template_name = 'templatesCreate/about.html'