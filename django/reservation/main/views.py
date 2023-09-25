from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm
# Create your views here.


def index(request):
    return render(request,template_name='main/index.html')

def dashboard(request):
    return render(request, template_name="main/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(request,template_name="main/register.html",context = {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse('main:dashboard'))