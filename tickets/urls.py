from django.urls import path, include
from tickets import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', views.viewsets_movie)

urlpatterns = [
    # path('movies/', views.MovieList.as_view()),
    # path('movies/<int:pk>', views.MovieDetails.as_view()),
    path('', include(router.urls))

    #path
]