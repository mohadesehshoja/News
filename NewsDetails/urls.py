from django.urls import path

from NewsDetails import views

urlpatterns=[
    path("magazineposts/",views.MagazineList.as_view(),name='magazine_list'),
    path('topicposts/',views.TopicList.as_view(),name='topic_list'),
    path('mynewposts/',views.MyNewList.as_view(),name='mynew_list'),
    path('magazineposts/<int:pk>',views.MagazineUporDe.as_view(),name="magzineuporde"),
    path('topicposts/<int:pk>',views.TopicUPorDe.as_view(),name="topicuporde"),
    path('mynewposts/<int:pk>',views.MyNewUporDe.as_view(),name="mynewuporde"),
]