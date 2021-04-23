from django.shortcuts import render , redirect
from  .models import Student
import requests


def index(request):
    return render (request,'mysite/index.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("Login Sucessfull")
        return redirect('mysite/join.html')
    else:
        print('user is not valid.')
        return render(request,'mysite/login.html')




def signup(request):
    if request.method == 'POST':
        fname_r = request.POST.get('fname')
        lname_r = request.POST.get('lname')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')

        data = Student(email = email_r, fname= fname_r, lname = lname_r, password=password_r)
        data.save()
        return render(request, 'mysite/login.html')
    else:
        return render(request, 'mysite/signup.html')

