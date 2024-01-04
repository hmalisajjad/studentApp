from django.contrib import admin
from .models import *
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email_address"]

@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["department_name"]
# Register your models here.
