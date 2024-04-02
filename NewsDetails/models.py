from django.db import models

from account.models import Profile


# Create your models here.

class Magazine(models.Model):
    name = models.CharField('name',max_length=70)
    builder = models.CharField('builder',max_length=80)
    address = models.TextField('address',max_length=150,null=True,blank=True)
    phone_number = models.CharField('phone number',unique=True,null=True,blank=True,max_length=20)
    website = models.URLField('website',blank=True,null=True)
    def __str__(self):
        return "{}-{}".format(self.name,self.builder)

class Topic(models.Model):
    topic=models.CharField('topic',max_length=150)
    def __str__(self):
        return self.topic

class MyNew(models.Model):
    title = models.CharField('title',max_length=250)
    body = models.TextField('body')
    footer=models.CharField('footer',max_length=250)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='mynews')
    magzine = models.ForeignKey(Magazine,on_delete=models.CASCADE,related_name='mynews')
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='mynews')
    date = models.DateTimeField('date',auto_now_add=True)
    def __str__(self):
        return "{}-{}".format(self.title,self.author.user.get_username())

