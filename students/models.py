from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.


gender = (('M', 'Male'), ('F', 'Female'))


class GradeClass(models.Model):
    grade_class = models.CharField(max_length=100)

    def __str__(self):
        return self.grade_class

    class Meta:
        ordering = ('grade_class', )


class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ('location', )


class Student(models.Model):
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100)
    grade_class = models.ForeignKey(GradeClass, on_delete=models.CASCADE)
    sex = models.CharField(max_length=100, choices=gender)
    dob = models.DateField(default=timezone.now, )
    house_no = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=100, default='', blank=True)
    email = models.EmailField(blank=True)
    phone1 = PhoneNumberField(region='ZW')
    phone2 = PhoneNumberField(region='ZW', blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        ordering = ('grade_class', 'sex', 'surname', )

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])
