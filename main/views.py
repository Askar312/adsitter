from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import render
from .serializers import PostSerializers, PostDetailSerializer
from rest_framework import generics
from .models import Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
<<<<<<< HEAD

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

=======
>>>>>>> 0933f8d30843d2eaed6a21abfd8f5f09790a751d
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request,'main/dashboard.html',{'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
<<<<<<< HEAD

                    return HttpResponse('Successful')
                else:
                    return HttpResponse('Ooops!')
            else:
                return HttpResponse('Register')
    else:
        form = LoginForm()
    return render(request, template_name='main/login.html', context={'form': form})

=======
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})
>>>>>>> 0933f8d30843d2eaed6a21abfd8f5f09790a751d

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'main/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def user_logout(request):
    logout(request)
    return redirect('login')


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializers

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser,)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

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


class BrowseAds(ListView):
    model = Post
    template_name = 'main/browse_ads.html'
    context_object_name = 'posts'

# class Clients(ListView):
#     template_name = 'main/clients.html'


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
