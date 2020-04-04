from django.urls import path

from post.views import post_index, post_create, post_delete, post_detail, post_update

app_name = 'post'

urlpatterns = [
    path('index/', post_index, name='index'),
    path('create/', post_create, name='create'),
    path('detail/<slug:slug>/', post_detail, name='detail'),
    path('update/<slug:slug>/', post_update, name='update'),
    path('delete/<slug:slug>/', post_delete, name='delete'),
]
