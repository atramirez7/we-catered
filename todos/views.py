from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoForm, TodoItemForm
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

def todo_list_create(request):
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

def todo_list_update(request, id):
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

def todo_list_delete(request, id):
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        list.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")

def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form
    }
    return render(request, "items/create.html", context)

def todo_item_update(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            model_instance = form.save()
            return redirect("todo_list_detail", id=model_instance.list.id)
    else:
        form = TodoItemForm(instance=item)
    context = {
        "item_detail": item,
        "form": form,
    }
    return render(request, "items/edit.html", context)
