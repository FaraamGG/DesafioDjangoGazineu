from django.db import models
from django.utils.timezone import now

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=65)


class Course(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    starts_at = models.DateTimeField(default=now)
    ends_at = models.DateTimeField(default=now)
    total_hours = models.IntegerField()
    more_info = models.TextField(default="")
    teacher = models.CharField(max_length=65)
    cover = models.ImageField(
        upload_to='institute/covers/')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
