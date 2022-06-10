from django.shortcuts import render
from django.views import generic

class HomeView(generic.TemplateView):
    template_name = 'templatesCreate/home.html'

class NewsView(generic.TemplateView):
    template_name = 'templatesCreate/news.html'

class SingleNewsView(generic.TemplateView):
    template_name = 'templatesCreate/single_news.html'

class AboutView(generic.TemplateView):
    template_name = 'templatesCreate/about.html'

class BlogView(generic.TemplateView):
    template_name = 'templatesCreate/blog.html'

class SingleBlogView(generic.TemplateView):
    template_name = 'templatesCreate/single_blog.html'

class ContactView(generic.TemplateView):
    template_name = 'templatesCreate/Contact.html'