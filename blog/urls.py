from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView,PostUpdateView,PostDeleteView



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'), #pk will refer to the models primary key, in this case the post  primary key
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'), #pk will refer to the models primary key, in this case the post  primary key
    path('post/new/',PostCreateView.as_view(), name='post-create'),
        path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
] 