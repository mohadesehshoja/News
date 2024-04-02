from django.contrib import admin

# Register your models here.
from django.contrib import admin

from NewsDetails.models import  Magazine, MyNew, Topic


admin.site.register(Magazine)
admin.site.register(Topic)
admin.site.register(MyNew)