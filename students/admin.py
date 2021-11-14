from django.contrib import admin
from .models import Student, GradeClass, Location
# Register your models here.


class StudentDisplay(admin.ModelAdmin):
    list_display = ('name', 'surname', 'grade_class')


admin.site.register(Student, StudentDisplay)


class ClassDisplay(admin.ModelAdmin):
    list_display = ['grade_class']


admin.site.register(GradeClass, ClassDisplay)
admin.site.register(Location)
