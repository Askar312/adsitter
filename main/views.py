from django.shortcuts import render, redirect
from .serializers import PostSerializers
from rest_framework import generics
from .models import Post
from .forms import *


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializers

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()




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
