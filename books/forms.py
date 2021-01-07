from books.models import Book
from django.forms import ModelForm

class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

