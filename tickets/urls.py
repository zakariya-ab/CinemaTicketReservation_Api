from django.urls import path
from tickets import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:pk>', views.MovieDetails.as_view()),
]