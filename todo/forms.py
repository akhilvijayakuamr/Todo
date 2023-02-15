from django import forms
from todo.models import Todo


class TodoForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your title'}))
    class Meta:
        model = Todo
        fields = ['title']
