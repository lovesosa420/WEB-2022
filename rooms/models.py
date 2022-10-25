from django.db import models


class Building(models.Model):
    name_building = models.CharField(max_length=30, primary_key=True)
    photo = models.ImageField(upload_to='images/buildings')


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    id_room = models.AutoField(primary_key=True)
    name_room = models.CharField(max_length=15)
    kind = models.CharField(max_length=35)
    size = models.IntegerField(max_length=3)
    price = models.IntegerField(max_length=5)
    is_free = models.BooleanField()
    photo = models.ImageField(upload_to='images/rooms')


class Customer(models.Model):
    customer_name = models.CharField(max_length=60, primary_key=True)
    phone = models.IntegerField(max_length=11)


class Rent(models.Model):
    number_rent = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()