from django.contrib import admin
from .models import SocialNetworks, Category, Post
from django_summernote.admin import SummernoteModelAdmin


class SocialNetworksAdmin(admin.ModelAdmin):
    list_display = ('social_network_name', 'social_network_link',)
    list_display_links = ('social_network_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug',)
    list_display_links = ('category_name',)


class PostAdmin(SummernoteModelAdmin):
    list_display = ('user', 'post_category', 'title',
                    'publication_date', 'update_date', 'published',)
    list_display_links = ('user', 'post_category', 'title',)
    list_editable = ('published',)
    summernote_fields = ('content',)


admin.site.register(SocialNetworks, SocialNetworksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
