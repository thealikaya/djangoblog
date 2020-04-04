from django.urls import path

from home.views import home_view, deneme

urlpatterns = [
    path('', home_view, name='home_view'),
    path('deneme/', deneme, name='deneme'),
]
