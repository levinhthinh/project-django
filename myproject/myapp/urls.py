from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.shop_content, name ='shop_content'),
    path('<int:kb_id>', views.shop_detail, name ='shop_detail'),
    # path('', views.book_list, name ='book_list'),
    # path('add/', views.add_info, name ='add_info'),
    # path('show/', views.show_info, name ='show_info')
]
if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)