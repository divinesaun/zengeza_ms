from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Student, GradeClass
from django.db.models import Q
from django.urls import reverse_lazy


# Create your views here.

def student_list(request):
    def is_valid_param(param):
        return param != '' and param is not None

    qs = Student.objects.all()
    gc = GradeClass.objects.all()
    name_contains = request.GET.get('name_or_surname')
    class_contains = request.GET.get('grade_class')
    if is_valid_param(name_contains):
        qs = qs.filter(Q(name__iregex=name_contains) |
                       Q(surname__iregex=name_contains)).distinct()

    if is_valid_param(class_contains) and class_contains != 'Choose...':
        qs = qs.filter(grade_class__grade_class__iexact=class_contains)

    con = {'queryset': qs,
           'gc': gc}
    return render(request, 'student list.html', con)


class StudentDetails(DetailView):
    model = Student
    template_name = 'student details.html'
    context_object_name = 'student'

