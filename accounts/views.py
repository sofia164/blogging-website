from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from blog.models import Profile
from .forms import ProfilePageForm


from blog.models import Post

from django.contrib.auth.decorators import login_required


class MyRegisterFormView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class UserProfileView(generic.DetailView):
    model = User
    template_name = 'accounts/profile.html'
    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'accounts/profile.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return render(request,'accounts/logout.html')


class UserEditFormView(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('blog:index')
    template_name = "accounts/edit_profile.html"

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('accounts:password_success')


def password_success(request):
    return render(request, 'accounts/password_success.html', {})


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile_page.html'
    success_url = reverse_lazy('blog:index')
    fields=['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url',]


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'accounts/create_profile_page.html'



    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
