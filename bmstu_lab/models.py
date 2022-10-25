from django.db import models


class Building_c(models.Model):
    name_building = models.CharField(max_length=30, primary_key=True)
    photo = models.ImageField(upload_to='images/buildings')


class Room_c(models.Model):
    building = models.ForeignKey(Building_c, on_delete=models.CASCADE)
    id_room = models.AutoField(primary_key=True)
    name_room = models.CharField(max_length=15)
    kind = models.CharField(max_length=35)
    size = models.IntegerField(max_length=3)
    price = models.IntegerField(max_length=5)
    photo = models.ImageField(upload_to='images/rooms')


class Customer_c(models.Model):
    customer_name = models.CharField(max_length=60, primary_key=True)
    phone = models.IntegerField(max_length=11)


class Rent_c(models.Model):
    number_rent = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room_c, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Customer_c, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()


