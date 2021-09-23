from django.db import models
from django.contrib.auth.models import User
# Create your models here.

import uuid
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
upload_storage = FileSystemStorage(location=settings.UPLOAD_ROOT, base_url='/profile_pic_dir')

def user_dir_profile_pic(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('profile_pic', ext)
    return '{0}/{1}'.format(instance.user.username, filename)

class UserStudent(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    
    M = 'Male'
    F = 'Female'
    CHOICES = [
        (M, 'Male'),
        (F, 'Female'),
    ]
    
    gender = models.CharField(max_length=6,choices=CHOICES,null=True)
    date_of_birth = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=300, null=True)
    FIRST = '1st'
    SECOND = '2nd'
    THIRD = '3rd'
    FOURTH = '4th'
    CHOICES1 = [
        (FIRST, '1st'),
        (SECOND, '2nd'),
        (THIRD, '3rd'),
        (FOURTH, '4th'),
    ]
    year = models.CharField(max_length=3,choices=CHOICES1,null=True)
    BA = 'Block-A'
    BB = 'Block-B'
    BC = 'Block-C'
    BD = 'Block-D'
    CHOICES2 = [
        (BA, 'Block-A'),
        (BB, 'Block-B'),
        (BC, 'Block-C'),
        (BD, 'Block-D'),
    ]
    block = models.CharField(max_length=7,choices=CHOICES2,null=True)
    BSCS = 'BSCS'
    CHOICES3 = [
        (BSCS, 'BSCS'),
    ]
    course = models.CharField(max_length=50,choices=CHOICES3, null=True)
    guardian_fname = models.CharField(max_length=200, null=True)
    guardian_cp_number = models.CharField(max_length=11, null=True)
    image1 = models.ImageField(upload_to=user_dir_profile_pic, storage=upload_storage, null=True, blank=True,)
    def __str__(self):
        return self.username


def user_dir_img1(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('image1', ext)
    return '{0}/{1}'.format(instance.user.username, filename)

def user_dir_img2(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('image2', ext)
    return '{0}/{1}'.format(instance.user.username, filename)

def user_dir_img3(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('image3', ext)
    return '{0}/{1}'.format(instance.user.username, filename)

def user_dir_img4(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('image4', ext)
    return '{0}/{1}'.format(instance.user.username, filename)

def user_dir_img5(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('image5', ext)
    return '{0}/{1}'.format(instance.user.username, filename)

def user_dir_img6(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('image6', ext)
    return '{0}/{1}'.format(instance.user.username, filename)

class UserImage(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    image1 = models.ImageField(upload_to=user_dir_img1, null=True, blank=True,)
    image2 = models.ImageField(upload_to=user_dir_img2, null=True, blank=True,)
    image3 = models.ImageField(upload_to=user_dir_img3, null=True, blank=True,)
    image4 = models.ImageField(upload_to=user_dir_img4, null=True, blank=True,)
    image5 = models.ImageField(upload_to=user_dir_img5, null=True, blank=True,)
    image6 = models.ImageField(upload_to=user_dir_img6, null=True, blank=True,)
    
    def __str__(self):
        return self.username
    
class Logbook(models.Model):
    id_number = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    cp_number = models.CharField(max_length=11, null=True)
    block = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)
    course = models.CharField(max_length=100, null=True)
    body_temp = models.CharField(max_length=100, null=True)
    body_temp_second_attempt = models.CharField(max_length=100, null=True)
    date_time_in = models.DateTimeField(null=True)
    date_time_exit = models.DateTimeField(null=True)
    remark = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.id_number
    

class SessionLogbook(models.Model):
    id_number = models.CharField(max_length=100, null=True)
    log_id = models.CharField(max_length=100, null=True)
    date_time_created = models.DateTimeField(null=True)
    date_time_expired = models.DateTimeField(null=True)
    def __str__(self):
        return self.id_number