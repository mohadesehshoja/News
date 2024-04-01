from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    name = models.CharField('full name',max_length=50)
    phone_number = models.IntegerField('phone number',blank=True,null=True)
    address = models.TextField(null=True, blank=True)
    male = 1
    fmale = 2
    gender = models.IntegerField('gender', choices=((male, 'male'), (fmale, 'fmale')), null=True, blank=True)
    profile_img = models.ImageField('image', null=True, blank=True, upload_to='users/profile_image')
    birth_date = models.DateTimeField('birth date',null=True,blank=True)
    def __str__(self):
        return self.name


