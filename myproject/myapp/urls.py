from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_info, name ='add'),
    path('/show', views.show_info, name ='show')
]
