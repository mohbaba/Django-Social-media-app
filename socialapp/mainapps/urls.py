from django.urls import path
from .views import index,signup,signin,logout,settings

urlpatterns = [
    path('', index ,name='index'),
    path('signup',signup, name = 'signup'),
    path('signin',signin, name = 'signin'),
    path('logout',logout, name = 'logout'),
    path('settings',settings, name = 'settings')
]