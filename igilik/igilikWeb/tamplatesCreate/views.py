from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .models import *

#done
class HomeView(ListView):
    model = Post
    context_object_name = "data"
    template_name = 'templatesCreate/home.html'

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').filter(singleType=1)[:3]
        return queryset

#done
class NewsView(ListView):
    model = Post
    template_name = 'templatesCreate/news.html'
    paginate_by = 4
    ordering = ['-time_create']

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').filter(singleType=1)
        return queryset

#done
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

#done
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
        context['user'] = self.request.user
        context['comments'] = Comments.objects.filter(~Q(id=(self.kwargs.get('pk')))).order_by('-id')[:2]
        return context

    def post(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        print(args)
        print(kwargs)
        return HttpResponseRedirect('/blog')


class SingleBlogView(generic.TemplateView):
    template_name = 'templatesCreate/single_blog.html'

#done
class MyBlogView(ListView):
    model = Post
    context_object_name = "data"
    template_name = 'templatesCreate/my_blog.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = Post.objects.order_by('-time_create').filter(user = self.request.user.id)
        return queryset

#done
class AddBlog(ListView):
    model = Post
    template_name = "templatesCreate/add_blog.html"

    def post(self, request, *args, **kwargs):
        userInfo = self.request.user
        titleInfo = self.request.POST['title']
        textInfo = self.request.POST['text']
        publicInfo = self.request.POST['public']
        imageIngo = self.request.POST['image']

        if publicInfo == str('on'):
            publicInfo = True
        else:
            publicInfo = False

        data = Post(title=titleInfo, content=textInfo, is_published=publicInfo, user=userInfo, image=imageIngo)
        data.save()

        return HttpResponseRedirect('/profile')

#done
class UpdataBlog(UpdateView):
    model = Post
    template_name = 'templatesCreate/update.html'
    fields = ['title', 'content', 'is_published', 'image']


class ContactView(generic.TemplateView):
    template_name = 'templatesCreate/Contact.html'

class ProfileView(generic.TemplateView):
    template_name = 'registration/profile.html'

class AboutView(generic.TemplateView):
    template_name = 'templatesCreate/about.html'