from django.shortcuts import render, redirect
from .serializers import PostSerializers
from rest_framework import generics
from .models import Post
from .forms import *
from django.shortcuts import render
from .serializers import PostSerializers, PostDetailSerializer
from rest_framework import generics
from .models import Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializers


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly)

def oauth(request):
    return render(request, 'index.html')


def index(request):
    return render(
        request,
        template_name='main/index.html'
    )

def about(request):
    return render(
        request,
        template_name='main/about.html'
    )

def browse_ads(request):
    return render(
        request,
        template_name='main/browse_ads.html'
    )

def clients(request):
    return render(
        request,
        template_name='main/clients.html'
    )

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            new = contact_form.save()
            return redirect('/')
    else:
        form = ContactForm()
    return render(
        request,
        'main/contact.html',
        {'form': form}
    )
