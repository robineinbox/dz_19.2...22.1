from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'slug', 'content', 'preview', 'published']


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'slug', 'content', 'preview', 'published']


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = '/blog/'


class BlogPostDetailView(DetailView):
    model = BlogPost
