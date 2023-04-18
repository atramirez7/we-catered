from django.shortcuts import render, get_object_or_404
from todos.models import TodoList
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
