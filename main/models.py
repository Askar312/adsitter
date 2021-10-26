from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

"""
-----------------
Contacts

Name
Email
Phone
Message
-----------------
-----------------
Post

Title
Image
Likes
Views
Created
Updated
Draft
Slug
User FK
Category FK
-----------------
_________________
Subcribe email -> Form (need)

Email
-----------------
-----------------
Category -> Form (need)

Title
Slug
-----------------
"""

class Contacts(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя заявителя'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('contacts', kwargs={'pk':self.pk})


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING,
        verbose_name='Категория'
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название поста',
        db_index=True
    )
    image = models.ImageField(
        upload_to='images/%Y/%m/%d',
        verbose_name='Фото'
    )
    likes = models.PositiveIntegerField(
        verbose_name='Лайки',
        default=0
    )
    views = models.PositiveIntegerField(
        verbose_name='Просмотры',
        default=0
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    draft = models.BooleanField(
        default=False,
        verbose_name='Черновик'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='Url',
        unique=True
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create_at']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug':self.slug})



class Subscribe(models.Model):
    email = models.EmailField(
        verbose_name='Email'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписчики'
        ordering = ['email']

    def __str__(self):
        return f"{self.email}"

    def get_absolute_url(self):
        return reverse('subscribe', kwargs={'pk':self.pk})




class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='Url',
        unique=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.slug})











