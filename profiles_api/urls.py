from django.urls import path

from profiles_api import views


urlpatterns = [

    path('helloApi', views.HelloApiView.as_view()),

]
