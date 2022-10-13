# Mengimpor modul-modul yang diperlukan
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime 
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/') # Merestriksi akses halaman todolist
def show_todolist(request):
    username = request.user.username
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    context = { 
        "username": username,
        "todolist": tasks
    }
    return render(request, "todolist_ajax.html", context)

def registrasi_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect("todolist:login_user")
    context = {"form":form}
    return render(request, "registration.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todolist:show_todolist")
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("todolist:login_user")

@login_required(login_url='/todolist/login/') # Merestriksi akses halaman create-task
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        newTask = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        newTask.save()
        return redirect("todolist:show_todolist")
    return render(request, "create_task.html")

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect("/todolist")

@login_required(login_url='/todolist/login/')
def update_status(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.is_finished = not task.is_finished
        task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@login_required(login_url='/todolist/login/') 
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(
            user=request.user,
            title=title, 
            description=description,
            date=datetime.now(),
            is_finished=False
        )

        context = {
            'pk':task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'date':task.date,
                'is_finished':task.is_finished,
            }
        }

    return JsonResponse(context)