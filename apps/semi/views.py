from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    print(users)
    return render(request, 'semi/users.html', context)

def create(request):
    user = User.objects.create(first_name=request.POST['first_name'],\
                        last_name=request.POST['last_name'],\
                        email=request.POST['email'])
    request.session['user_id'] = user.id
    print(request.POST.values())
    return redirect('/')

def add(request):   
    return render(request,'semi/add.html')

def edit_user(request, id):
    edit_v = User.objects.get(id=id)
    edit_v.first_name=request.POST['first_name']
    edit_v.last_name=request.POST['last_name']
    edit_v.email=request.POST['email']
    edit_v.save()
    print (edit_v)
    return redirect('/')

def edit(request, id):
    users = User.objects.get(id=id)
    context = {
        'user': users
    }
    return render(request, 'semi/edit.html', context)

def profile(request):
    return render(request, 'semi/profile.html')

def show_profile(request, id):
    users = User.objects.get(id=id)
    context = {
        'user': users
    }
    return render(request, 'semi/profile.html', context)

def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')