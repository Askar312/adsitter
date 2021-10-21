from django.urls import path
from .views import index, PostListView, PostCreateView, PostDetailView


urlpatterns = [
    path('', index),
    path('api/v1/post-list/', PostListView.as_view()),
    path('api/v1/post-create/', PostCreateView.as_view()),
    path('api/v1/post-detail/<int:pk>/', PostDetailView.as_view())
]