from django.db import models


YEAR_CHOICES=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)

class People(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    semester = models.IntegerField(choices=YEAR_CHOICES, blank=False)
    Department = models.CharField(max_length=70, blank=False)
    linkedin = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)
    # photo = ProcessedImageField(upload_to='post_images', blank=False)
