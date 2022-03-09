from django.contrib import admin

from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Tag, Article

admin.site.register(Tag)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    # docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    # books.agiliq.com/projects/django-admin-cookbook/en/latest/current_user.html
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    list_display = ('title',)

    list_filter = ('tags', 'created_time',)

    search_fields = ('title', 'body',)


admin.site.register(Article, ArticleAdmin)