from django.shortcuts import render, redirect
from django.views.generic import FormView

from library import forms


def home_view(request):
    # courses = Course.objects.all()
    return render(request, 'home.html', {
        # 'courses': courses,
        'active': 'home'
    })


class SiteCreateCategory(FormView):
    template_name = 'category/create_category.html'
    form_class = forms.CreateCategoryForm

    def form_valid(self, form):
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(SiteCreateCategory, self).get_context_data(**kwargs)
        context['active'] = 'create_category'
        return context


class SiteCreateBook(FormView):
    template_name = 'book/create_book.html'
    form_class = forms.CreateBookForm

    def form_valid(self, form):
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(SiteCreateBook, self).get_context_data(**kwargs)
        context['active'] = 'create_book'
        return context
