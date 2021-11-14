from django.urls import path
from .views import student_list, StudentDetails

urlpatterns = [
    path('', student_list, name='list'),
    path('<int:pk>/', StudentDetails.as_view(), name='details'),
]
