from django.urls import path
from todos.views import todo_list_list, todo_list_detail, add_todo, edit_todo

urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create", add_todo, name="add_todo"),
    path("<int:id>/edit/", edit_todo, name='edit_todo'),
]
