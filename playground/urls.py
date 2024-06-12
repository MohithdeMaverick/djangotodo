from django.urls import path
from . import views
from .views import  home

urlpatterns=[
    path('', home,name='home'),
    path('about/', views.bc, name='about_page'),
    path('del-sub/<int:subid>/',views.dele,name='del-sub')
    #path('hello/',home),
]