from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


gender = (('Male', 'Male'), ('Female', 'Female'))


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
    dob = models.DateField(default='2007-12-31', )
    house_no = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone1 = PhoneNumberField(region='ZW')
    phone2 = PhoneNumberField(region='ZW', blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        ordering = ('grade_class', 'sex', 'surname', )

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])
