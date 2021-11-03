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
    save_on_top = True


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

    save_on_top = True


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'slug',)
    save_on_top = True


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
<<<<<<< HEAD
admin.site.register(Category, CategoryAdmin)
=======

admin.site.register(Category, CategoryAdmin)

>>>>>>> 0933f8d30843d2eaed6a21abfd8f5f09790a751d
