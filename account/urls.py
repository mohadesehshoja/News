
from django.urls import path

from account import views
from account.views import ProfileList
urlpatterns=[
    path('profileposts/',views.ProfileList.as_view(),name='profile_list'),
    path('profileposts/<int:pk>',views.ProfileListUpDestroy.as_view(),name='profile_UpDe'),
    path('Registerform/',views.RegisterAPI.as_view(),name='register_api'),
    path('loginform/',views.loginAPI.as_view(),name='login_api'),
]