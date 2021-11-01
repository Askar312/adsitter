from django.contrib import admin
from .models import *


# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'phone',
                    'message',
                    )

    list_filter = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'category',
                    'title',
                    'image',
                    'likes',
                    'views',
                    'create_at',
                    'update_at',
                    'draft',
                    'slug',

                    )

    list_filter = ('user',
                   'title',)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'slug',)


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Category, CategoryAdmin)
