from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name ='shop'),
    # path('', views.book_list, name ='book_list'),
    # path('add/', views.add_info, name ='add_info'),
    # path('show/', views.show_info, name ='show_info')
]
