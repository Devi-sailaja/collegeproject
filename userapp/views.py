from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def register(request):
        if request.method=='POST':
                form = FarmstoreForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('farm_list') 
        else:
                form = FarmstoreForm()
        return render(request,'register.html',{'form':form})
def farm_list(request):
        farmstore= Farmstore.objects.all()
        return render(request,'farm_list.html',{'farmstore':farmstore})
def home(request):
         return render(request,'index.html')
def register_cust(request):
        if request.method=="POST":
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        username=form.cleaned_data['username']
                        email=form.cleaned_data['email']
                        password=form.cleaned_data['password']
                        User.objects.create_user(username=username,email=email,password=password)
                        return redirect('home')
        else:
                form = RegistrationForm()
        return render(request,'register_cust.html',{'form':form})
def user_login(request):
        if request.method == 'POST':
                form = AuthenticationForm(request,data=request.POST)
                if form.is_valid():
                        username = form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password')
                        user = authenticate(username=username,password=password)
                        if user is not None:
                                login(request, user)
                                return redirect('home')
        else:
                form = AuthenticationForm()
        return render(request,'user_login.html',{'form':form})
def user_logout(request):
        logout(request)
        return redirect('home')




def about(request):
        return render(request,'about.html')
def service(request):
        return render(request,'service.html')
def product(request):
        return render(request,'product.html')
def contact(request):
        return render(request,'contact.html')
def team(request):
        return render(request,'team.html')
def testimonial(request):
        return render(request,'testimonial.html')
def feature(request):
        return render(request,'feature.html')
def blog(request):
        return render(request,'blog.html')
def detail(request):
        return render(request,'detail.html')