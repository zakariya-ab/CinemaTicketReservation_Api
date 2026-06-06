from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    duration = models.IntegerField()
    language = models.CharField(max_length=100)
    age_rating = models.CharField(max_length=10)
    release_date = models.DateField()
    poster_url = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


class Cinema(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    adress = models.CharField(max_length=400)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    total_rows = models.IntegerField()
    seats_per_row = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cinema', 'name'],
                name= 'unique_cinema_room'
            )

        ]


class Seat(models.Model):
    class Types(models.TextChoices):
        NORMAL = 'normal'
        VIP = 'vip'
        
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    row = models.CharField(max_length = 5)
    number = models.IntegerField()
    seat_type = models.CharField(
        max_length=10,
        choices=Types.choices,
        default=Types.NORMAL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['room', 'row', 'number'],
                name = 'unique_room_row_seat'
            )
        ]


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  


class User(AbstractUser):
    pass


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.PENDING
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  


class ReservationSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  



class Payment(models.Model):
    class PayemntMethodes(models.TextChoices):
        CARD = 'card'
        CASH = 'cash'
        WALLET = 'wallet'
    
    class PaymentStatus(models.TextChoices):
        PENDING = 'pending'
        SUCCESS = 'success'
        FAILED = 'failed'

    
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    methode = models.CharField(
        max_length=30,
        choices=PayemntMethodes.choices,
        default=PayemntMethodes.CASH
    )
    status = models.CharField(
        max_length=40,
        choices = PaymentStatus.choices,
        default= PaymentStatus.PENDING
    )
    transaction_id = models.CharField(max_length=100, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

