from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('events/', views.events, name='events'),
    path('charter/', views.charterHeader, name='citizen'),
    path('gallery/', views.gallery, name='gallery'),
    path('media/', views.media, name='media'),
    path('awards/', views.awards, name='awards'),
]

