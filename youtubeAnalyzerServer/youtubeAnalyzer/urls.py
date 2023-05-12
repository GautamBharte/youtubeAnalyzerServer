from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post/', views.postRequest, name='create_post'),
    path('get/<str:name>/', views.GetRequest, name='my_api'),
]
