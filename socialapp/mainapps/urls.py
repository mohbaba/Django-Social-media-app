from django.urls import path
from .views import index,signup,signin,logout,settings,upload,like_post

urlpatterns = [
    path('', index ,name='index'),
    path('upload',upload,name='upload'),
    path('like-post',like_post,name='like-post'),
    path('signup',signup, name = 'signup'),
    path('signin',signin, name = 'signin'),
    path('logout',logout, name = 'logout'),
    path('settings',settings, name = 'settings'),
]