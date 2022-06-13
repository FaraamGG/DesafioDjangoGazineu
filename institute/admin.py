from django.contrib import admin

from .models import Course

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    ...


admin.site.register(Course, CourseAdmin)
