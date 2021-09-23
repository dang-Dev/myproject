from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserStudent, UserImage

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model= User
        fields = ['old_password', 'new_password1', 'new_password2']
        
class UserStudentForm(ModelForm):
    class Meta:
        model = UserStudent
        exclude = ('date_created',)
        widgets = {
            'date_of_birth': forms.DateInput,
        }
        fields = ['first_name', 'middle_name', 'last_name', 'email','age','gender','address','contact_number', 'date_of_birth','guardian_fname', 'guardian_cp_number', 'course', 'year', 'block']
        
class UserImageForm(ModelForm):
    class Meta:
        model = UserImage
        fields = ['image1', 'image2','image3','image4','image5','image6',]
