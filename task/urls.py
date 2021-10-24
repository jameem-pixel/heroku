from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home, name="home"),
    path('myproject/',views.Project,name="myproject"),
    path('viewp/<str:pk>/',views.Toview,name="viewp"),
]