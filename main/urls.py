from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('clients/', clients, name='clients'),
    path('contact/', contact, name='contact'),
    path('browse_ads/', BrowseAds.as_view(), name='browse_ads'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('api/v1/post-list/', PostListView.as_view()),
    path('api/v1/post-create/', PostCreateView.as_view()),
    path('api/v1/post-detail/<int:pk>/', PostDetailView.as_view()),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)