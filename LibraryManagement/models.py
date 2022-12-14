from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.
#class addstudent(models.Model):
    #studentName = models.CharField(max_length=20)
    #studentAge = models.IntegerField()


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bookName = models.CharField(max_length=20)
    bookAuthor = models.CharField(max_length=20)
    bookGenre = models.CharField(max_length=20)
    image = models.ImageField(null=True, upload_to='images/')
    rented = models.BooleanField(default=False, null=True, blank=True)

def get_returndate():
    return datetime.today() + timedelta(days=14)


class RentBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    dateIssued = models.DateTimeField(auto_now_add=True)
    dateDue = models.DateTimeField(default=get_returndate())


