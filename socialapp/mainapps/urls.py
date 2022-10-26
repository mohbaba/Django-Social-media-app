from django.urls import path
from .views import index,signup,signin,logout,settings,upload,like_post,profile

urlpatterns = [
    path('', index ,name='index'),
    path('upload',upload,name='upload'),
    path('like-post',like_post,name='like-post'),
    path('signup',signup, name = 'signup'),
    path('profile/<str:pk>',profile, name = 'profile'),
    path('signin',signin, name = 'signin'),
    path('logout',logout, name = 'logout'),
    path('settings',settings, name = 'settings'),
]