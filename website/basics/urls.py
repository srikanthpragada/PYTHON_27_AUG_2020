
from django.urls import path
from . import views, interest_views

urlpatterns = [
    path('welcome', views.welcome),
    path('topics', views.topics),
    path('list_topics', views.send_topics),
    path('wish', views.wish),
    path("interest", interest_views.interest),
]
