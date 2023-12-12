from django.contrib import admin
from .models import student,userOtp
# Register your models here.

@admin.register(userOtp)
class otp(admin.ModelAdmin):
    list_display=['id','otp','username']
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']


