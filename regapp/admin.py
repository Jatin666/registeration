from django.contrib import admin
from regapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list = ['NO','Name','Age','Mob','Email','Add']

admin.site.register(Student,StudentAdmin)