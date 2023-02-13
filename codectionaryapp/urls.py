from django.contrib import admin
from django.urls import path, include
from codectionaryapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('watch', views.watchpage, name='watch'),
    path('login', views.login, name='login'),
    path('profile/<str:publisher>/', views.profile, name='profile'),
    path('studio', views.studio, name='studio'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('videos', views.videos, name='videos'),
    path('upload', views.uploadContent, name='uploadvideo'),
    path('updatevideo', views.updateVideo, name='update'),
    path('like', views.like, name='like'),
    path('save', views.save, name='save'),
    path('follow', views.follow, name='follow'),
    path('unfollow', views.unfollow, name='unfollow'),
    path('comment', views.comment, name='comment'),
    path('saved', views.saved, name='saved'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('delete', views.deleteVideo, name='delete'),
    path('earning', views.earning, name='earning'),
]
