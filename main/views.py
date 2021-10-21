from django.shortcuts import render
from .serializers import PostSerializers
from rest_framework import generics
from .models import Post
# Create your views here.
def index(request):
    return render(
        request,
        template_name='main/index.html'
    )

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializers

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()