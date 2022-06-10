from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news', NewsView.as_view(), name='news'),
    path('singleNews', SingleNewsView.as_view(), name='singleNews'),
    path('blog', BlogView.as_view(), name='blog'),
    path('singleBlog', SingleBlogView.as_view(), name='singleBlog'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
]