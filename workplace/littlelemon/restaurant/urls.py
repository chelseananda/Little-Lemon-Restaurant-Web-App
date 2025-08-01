from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('', views.home, name='home'),
]