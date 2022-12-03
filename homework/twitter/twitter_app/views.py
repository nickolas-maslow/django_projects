from django.shortcuts import render

from .models import User
from .services import add_user
from django.views.generic import ListView
from twitter_app.models import User
from django.core.paginator import Paginator


def listing(request):
    contact_list = User.objects.all()
    paginator = Paginator(contact_list, 25) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})
class UserListView(ListView):
    paginate_by = 2
    model = User

class ESearchView(View):
    template\_name = 'search/index.html'
 
    def get(self, request, *args, **kwargs):
        context = {}
 
        question = request.GET.get('q')
        if question is not None:
            search\_articles = Article.objects.filter(article\_content\_\_search=question)
            context['last\_question'] = '?q=%s' % question
 
            current\_page = Paginator(search\_articles, 10)
 
            page = request.GET.get('page')
            try:
                context['article\_lists'] = current\_page.page(page)
            except PageNotAnInteger:
                context['article\_lists'] = current\_page.page(1)
            except EmptyPage:
                context['article\_lists'] = current\_page.page(current\_page.num\_pages)
 
        return render\_to\_response(template\_name=self.template\_name, context=context)


def index(request):
    return render(request, 'index.html')


def log_in(request):
    return render(request, 'login.html')


def sign_up(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        first_password = request.POST.get('firstpassword')
        second_password = request.POST.get('secondpassword')
        return add_user(login, first_password, second_password)

    return render(request, 'signup.html')


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


