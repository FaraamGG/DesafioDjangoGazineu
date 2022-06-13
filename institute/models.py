from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    duration = models.IntegerField()
    duration_unit = models.CharField(max_length=65)
    total_hours = models.IntegerField()
    professor = models.CharField(max_length=65)
    cover = models.ImageField(upload_to='institute/static/images/courses_img')

    def __str__(self):
        return self.title
