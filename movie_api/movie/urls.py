from django.urls import path
from movie import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/', views.MovieList, name='api'),
    path('api/create/', views.MovieCreate, name="api_create"),
    path('api/update/<str:pk>/', views.MovieUpdate, name="api_update"),
    path('api/delete/<str:pk>/', views.MovieDelete, name="api_delete"),
]