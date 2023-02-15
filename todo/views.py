from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import *

# Create your views here.

def home(request):
    form=TodoForm()
    todos=Todo.objects.all()
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form,'todos':todos}
    return render(request,"home.html",context)

def update(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    form=TodoForm(instance=todo)
    if request.method == 'POST':
        form=TodoForm(request.POST ,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,"update.html",context)


def delete(request,todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=todo_id).delete()
        return redirect('home')
