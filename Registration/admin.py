from django.contrib import admin
from .models import UserStudent, UserImage, Logbook
# Register your models here.
@admin.register(UserStudent)
class UserStudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'date_of_birth')

@admin.register(UserImage)  
class UserImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6',)
    
@admin.register(Logbook)  
class LogbookAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'first_name', 'middle_name', 'last_name', 'age', 'gender', 'address', 'block', 'year', 'course', 'body_temp', 'date_time_in', 'date_time_exit')
    