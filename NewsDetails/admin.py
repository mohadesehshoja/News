from django.contrib import admin

# Register your models here.
from django.contrib import admin

from NewsDetails.models import Writter, Magazine, MyNews, Topics

admin.site.register(Writter)
admin.site.register(Magazine)
admin.site.register(Topics)
admin.site.register(MyNews)