from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/images/")
    brief = models.CharField(250)
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    venue = models.CharField(100)
    description = models.TextField()
    created_at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class EventStatus(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status