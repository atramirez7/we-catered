from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoForm
# Create your views here.

def todo_list_list(request):
    todolist = TodoList.objects.all()
    count = TodoList.objects.count()
    context = {
        "todo_list_list": todolist,
        "count": count,
    }
    return render(request, "todos/list.html", context)

def todo_list_detail(request, id):
    todo_detail = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": todo_detail,
    }
    return render(request, "todos/detail.html", context)

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoForm()
    context = {
        "form": form
    }
    return render(request, "todos/create.html", context)

def edit_todo(request, id):
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoForm(instance=list)
    context = {
        "todo_list_detail": list,
        "form": form,
    }
    return render(request, "todos/edit.html", context)

def delete_todo(request, id):
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        list.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")
