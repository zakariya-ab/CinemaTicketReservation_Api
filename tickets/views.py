"""
Function based views
"""

# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Guest
# from .serializers import GuestSerializer


# # Create your views here.

# @api_view(['GET', 'POST'])
# def guests_list(request):
#     if request.method == 'GET':
#         guests = Guest.objects.all()
#         serializer = GuestSerializer(guests, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = GuestSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def guest_details(request, pk):
#     try:
#         guest = Guest.objects.get(pk=pk)
#     except Guest.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer = GuestSerializer(guest)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = GuestSerializer(guest, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         serializer = GuestSerializer(guest)
#         guest.delete()
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

"""
    Class based views
"""

# from tickets.models import Movie
# from tickets.serializers import MovieSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status 

# class MovieList(APIView):

#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=all)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         Response(status = status.HTTP_400_BAD_REQUEST)

# class MovieDetails(APIView):
    
#     def get_object(self, pk):
#         try:
#             return Movie.objects.get(pk = pk)
#         except Movie.DoesNotExist:
#             return Response(Http404)

#     def get(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    
#     def put(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(status = status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
        
"""
    class based views (using mixins)
"""

# from tickets.models import Movie
# from tickets.serializers import MovieSerializer
# from rest_framework import mixins, generics

# class MovieList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class MovieDetails(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

"""
    generic class-based views
"""

# from tickets.models import Movie
# from tickets.serializers import MovieSerializer
# from rest_framework import generics

# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

"""
    viewsets
"""

from .models import *
from .serializers import *
from rest_framework import viewsets

class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class viewsets_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class viewsets_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class viewsets_cinema(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class viewsets_room(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class viewsets_screening(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer

class viewsets_seat(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


