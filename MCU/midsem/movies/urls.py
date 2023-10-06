from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [

    path('', views.logins,name='logins'),
    path('register/', views.register,name='register'),
    path('home/', views.home, name='home'),
    path('logout', views.logout),
    path('main/', views.main, name='main'),
    #path('homepage', views.homepage,name='homepage'),
    path('success_page/', views.success_page, name='success_page'),
    path('m1/', views.m1, name='m1'),
    path('m2/', views.m2, name='m2'),
    path('m3/', views.m3, name='m3'),
    path('m4/', views.m4, name='m4'),
    path('m5/', views.m5, name='m5'),
    path('m6/', views.m6, name='m6'),
    path('m7/', views.m7, name='m7'),
    path('m8/', views.m8, name='m8'),
    path('m9/', views.m9, name='m9'),
    path('m10/', views.m10, name='m10'),
    path('about/', views.about, name='about'),    
]