from django.db import models

# Create your models here.
class Writter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField( unique=True,null=True,blank=True)
    def __str__(self):
        return self.name

class Magazine(models.Model):
    name = models.CharField('name',max_length=70)
    builder = models.CharField('builder',max_length=80)
    address = models.CharField('address',max_length=150,null=True,blank=True)
    phone_number = models.IntegerField('phone number',unique=True,null=True,blank=True)
    money = models.IntegerField('money')
    website = models.URLField('website',blank=True,null=True)
    def __str__(self):
        return "{}-{}".format(self.name,self.builder)

class Topics(models.Model):
    topic=models.CharField('topic',max_length=150)
    def __str__(self):
        return self.topic

class MyNews(models.Model):
    title = models.CharField('title',max_length=100)
    body = models.TextField('body')
    author = models.ForeignKey(Writter,on_delete=models.CASCADE)
    magzine = models.ForeignKey(Magazine,on_delete=models.CASCADE)
    topic = models.OneToOneField(Topics,on_delete=models.CASCADE)
    date = models.DateTimeField('date',auto_now_add=True)
    def __str__(self):
        return "{}-{}".format(self.title,self.author.name)

