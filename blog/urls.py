from django.urls import path
from .views import BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, BlogPostDetailView

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blog_update'),
    path('<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
    path('<slug:slug>/', BlogPostDetailView.as_view(), name='blog_detail'),
]