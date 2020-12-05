from django import forms
from .models import Book

class BookCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Book
        fields = '__all__'