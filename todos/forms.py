from django.forms import ModelForm, forms
from todos.models import TodoList, TodoItem

class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = (
            "name",
        )

class TodoItem(ModelForm):
    class Meta:
        model = TodoItem
        fields = {
            "task",
            "due_date",
            "is_completed",
            "list",
        }
