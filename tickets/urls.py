from django.urls import path, include
from tickets import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', views.viewsets_movie)
router.register('users', views.viewsets_user)
router.register('reservations', views.viewsets_reservation)
router.register('cinemas', views.viewsets_cinema)
router.register('rooms', views.viewsets_room)
router.register('screenings', views.viewsets_screening)
router.register('seats', views.viewsets_seat)


urlpatterns = [
    # path('movies/', views.MovieList.as_view()),
    # path('movies/<int:pk>', views.MovieDetails.as_view()),
    path('', include(router.urls))

    #path
]