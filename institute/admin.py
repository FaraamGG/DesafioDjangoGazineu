from django.contrib import admin

from .models import Course, Teacher

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    ...


class TeacherAdmin(admin.ModelAdmin):
    ...


admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
