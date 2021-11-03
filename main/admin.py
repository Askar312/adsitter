from django.contrib import admin
from .models import *


# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'phone',
                    'message',)
    list_filter = ('name',)
    save_on_top = True


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('user',
                    'category',
                    'title',
                    'image',
                    'likes',
                    'views',
                    'create_at',
                    'update_at',
                    'draft',
                    'slug',)
    list_filter = ('user',
                   'title',)
    save_on_top = True


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title',
                    'slug',)
    save_on_top = True

class ClientsReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',
                    'image',
                    'review',
                    'create_at',
                    'user',
                    'slug',)
    list_filter = ('name',)
    save_on_top = True


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ClientsReview, ClientsReviewAdmin)

