from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")

    def __str__(self):
        return self.name


class Event(models.Model):

    class StatusChoices(models.TextChoices):
        UPCOMING = 'Upcoming', 'Upcoming'
        ON_SHOW = 'OnShow', 'On Show'
        PREVIOUS = 'PreviousEvent', 'Previous Event'

    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)
    brief = models.CharField(max_length=250, verbose_name="Brief Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")
    views_count = models.PositiveIntegerField(default=0, editable=False)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.UPCOMING
    )
    created_at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date', 'start_time']
        verbose_name = "Event"
        verbose_name_plural = "Events"