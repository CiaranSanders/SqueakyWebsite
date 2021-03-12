from django.urls import path

from . import views

app_name = 'meow'

urlpatterns = [
   path('test/', views.test),
]
