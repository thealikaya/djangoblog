from django.contrib import admin
from post.models import Post



class PostModel(admin.ModelAdmin):
    list_display = ('title', 'publishing_date', 'slug')
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ('title', 'content')
    list_editable = ['title']


admin.site.register(Post, PostModel)
