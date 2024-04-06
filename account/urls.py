
from django.urls import path

from account import views
from account.views import ProfileList
urlpatterns=[
    path('profileposts/',views.ProfileList.as_view(),name='profile_list')
]