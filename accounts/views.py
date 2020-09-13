from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
        return render(request, 'accounts/login.html', {'form': form})

class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse('accounts:login')


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('home')