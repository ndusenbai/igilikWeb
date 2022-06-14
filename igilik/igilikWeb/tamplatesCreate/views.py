from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView

from .models import *


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'templatesCreate/home.html'

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').all()[:3]
        return queryset


class NewsView(ListView):
    model = Post
    template_name = 'templatesCreate/news.html'
    paginate_by = 4
    ordering = ['-time_create']

class SingleNewsView(DetailView):
    model = Post
    template_name = 'templatesCreate/single_news.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(SingleNewsView, self).get_context_data(**kwargs)
        context['data'] = 'goBack'
        return context


class AboutView(generic.TemplateView):
    template_name = 'templatesCreate/about.html'

class BlogView(generic.TemplateView):
    template_name = 'templatesCreate/blog.html'

class SingleBlogView(generic.TemplateView):
    template_name = 'templatesCreate/single_blog.html'

class ContactView(generic.TemplateView):
    template_name = 'templatesCreate/Contact.html'

class ProfileView(generic.TemplateView):
    template_name = 'registration/profile.html'

class MyBlogView(generic.TemplateView):
    template_name = 'templatesCreate/my_blog.html'