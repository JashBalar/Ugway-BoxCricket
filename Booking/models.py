from django.db import models
from django.contrib.auth.models import User



class Turf(models.Model):
    name = models.CharField(max_length=100, unique=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    landmark = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    length = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='turf_images')
    total_nets = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.IntegerField(default=1000)
    verified = models.BooleanField(default=False)
    object = models.manager

    def __str__(self):
        return self.name + ' - ' + self.city



class Rating(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    rating_1_count = models.PositiveSmallIntegerField(default=0)
    rating_2_count = models.PositiveSmallIntegerField(default=0)
    rating_3_count = models.PositiveSmallIntegerField(default=0)
    rating_4_count = models.PositiveSmallIntegerField(default=0)
    rating_5_count = models.PositiveSmallIntegerField(default=0)
    object = models.manager

    def __str__(self):
        return self.turf.name


class Timings(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    price = models.PositiveSmallIntegerField()
    object = models.manager

    def __str__(self):
        return self.turf.name


class Booking(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price = models.PositiveSmallIntegerField()
    object = models.manager

    def __str__(self):
        return str(self.user)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=10)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    object = models.manager

    def __str__(self):
        return self.user.username
