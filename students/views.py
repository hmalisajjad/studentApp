from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    students = None
    return render(request,'home.html',{'students':students})

def student(request, student_id):
    student = None
    return render(request,'student.html',{'student':student})