from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name='index'),
    path('search',search, name = 'search'),
    path('follow', follow ,name='follow'),
    path('upload',upload,name='upload'),
    path('like-post',like_post,name='like-post'),
    path('signup',signup, name = 'signup'),
    path('profile/<str:pk>',profile, name = 'profile'),
    path('signin',signin, name = 'signin'),
    path('logout',logout, name = 'logout'),
    path('settings',settings, name = 'settings'),
]