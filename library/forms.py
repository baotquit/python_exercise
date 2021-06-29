from django.forms import ModelForm
from django import forms
from library.models import Category, Book

AVAILABLE = 0
BORROWED = 1
STATUS_CHOICES = (
    (AVAILABLE, 'Available'),
    (BORROWED, 'Borrowed'),
)


class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class CreateBookForm(ModelForm):
    status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                       choices=STATUS_CHOICES)

    class Meta:
        model = Book
        fields = ('name', 'categories', 'status', 'quantity')
        widgets = {
            'categories': forms.Select(),
        }
