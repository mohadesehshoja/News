from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    phone_number = models.CharField('phone number',blank=True,null=True,max_length=20)
    address = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=5)
    male = 1
    fmale = 2
    gender = models.IntegerField('gender', choices=((male, 'male'), (fmale, 'fmale')), null=True, blank=True)
    profile_img = models.ImageField('image', null=True, blank=True, upload_to='users/profile_image')
    birth_date = models.DateTimeField('birth date',null=True,blank=True)
    def __str__(self):
        return self.user.get_username()


