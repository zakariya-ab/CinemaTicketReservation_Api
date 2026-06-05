from django.urls import path
from tickets import views

urlpatterns = [
    path('guests/', views.guests_list),
    path('guests/<int:pk>', views.guest_details),
]