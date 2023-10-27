from django.contrib import admin
from django.urls import path,include
from todo import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add,name="add"),
    path('delete/<int:todoid>',views.dele,name="dele")
]
