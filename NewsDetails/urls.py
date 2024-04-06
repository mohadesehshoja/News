from django.urls import path

from NewsDetails import views

urlpatterns=[
    path("magazineposts/",views.MagazineList.as_view(),name='magazine_list'),
    path('topicposts/',views.TopicList.as_view(),name='topic_list'),
    path('mynewposts/',views.MyNewList.as_view(),name='mynew_list'),
]