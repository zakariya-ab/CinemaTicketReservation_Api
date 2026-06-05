from rest_framework import serializers
from .models import Movie, Guest, Reservation

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        # fields = ['id', 'name', 'mobile']
        fields = '__all__'