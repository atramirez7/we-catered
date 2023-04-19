from django.forms import ModelForm, forms
from todos.models import TodoList

class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = (
            "name",
        )
