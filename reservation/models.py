from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from car.models import Car, Category
from home.models import UserProfile


class Reservation(models.Model):
    Status = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    code = models.CharField(max_length=5, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=10, blank=True)
    rezdate = models.DateField()
    returndate = models.DateField()
    days = models.IntegerField(blank=True)
    price = models.IntegerField(null=True)
    total = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=Status, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'first_name', 'last_name', 'rezdate', 'returndate']
