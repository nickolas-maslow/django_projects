from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='not_logged_homepage'),
    path('login/', log_in, name='login'),
    path('signup/', sign_up, name='signup'),
    path('write_comment/', write_comment, name='comment'),
    path('edit_post/', edit_post, name='edit_post'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('my_followers/', my_followers, name='my_followers'),
    path('my_following/', my_following, name='my_following'),
    path('home/', home, name='logged_homepage'),
    path('my_profile/', my_profile, name='my_profile'),
    path('user_profile/', user_profile, name='user_profile'),
    path('user_followers/', user_followers, name='user_followers'),
    path('user_followings', user_followings, name='user_followings'),
]