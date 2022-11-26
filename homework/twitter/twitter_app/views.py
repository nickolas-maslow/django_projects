from django.shortcuts import render
from .services import add_user


def index(request):
    return render(request, 'index.html')


def log_in(request):
    return render(request, 'login.html')


def sign_up(request):
    context = {'add_user': add_user(user_login=request.POST())}
    return render(request, 'signup.html', context=context)


def write_comment(request):
    return render(request, 'comment_section.html')


def edit_post(request):
    return render(request, 'edit_post.html')


def edit_profile(request):
    return render(request, 'edit_profile.html')


def my_followers(request):
    return render(request, 'my_followers.html')


def my_following(request):
    return render(request, 'my_following.html')


def home(request):
    return render(request, 'home.html')


def my_profile(request):
    return render(request, 'profile.html')


def user_profile(request):
    return render(request, 'user_profile.html')


def user_followers(request):
    return render(request, 'user_followers.html')


def user_followings(request):
    return render(request, 'user_following.html')


