from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="facemask_home"),
    path('video', views.video,name="video"),
]
