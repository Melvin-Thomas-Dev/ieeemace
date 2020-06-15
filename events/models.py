from django.db import models
# from imagekit.models import ProcessedImageField
# from datetime import datetime


event_type_choices = (
    ('Competition','competition'),
    ('workshop','workshop'),
    ('webinar','webinar'),
    ('talk session','talk session'),
    ('peer to peer','peer to peer'),
    ('miscellaneous','miscellaneous'),
    ('other','other')
)
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=150, blank=False)
    event_type = models.CharField(max_length=200,choices=event_type_choices)
    slug = models.SlugField(max_length=200, blank=False, unique=True, default='slug')
    brief = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=False, default=' ')
    date = models.CharField(max_length=100, blank=False)
    fees = models.TextField(max_length=50, blank=True)
    prize = models.TextField(max_length=50, blank=True)
    # cover = ProcessedImageField(upload_to='post_images', blank=False)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
