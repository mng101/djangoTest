from django.shortcuts import render

from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DetailView, )

from . import forms
from .forms import StockForm
from .models import Stock

from . import forms

# Create your views here.

class HomePageView(TemplateView):
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("home")
    template_name = "myapp/signup.html"


class ThanksPageView(TemplateView):
    template_name = 'myapp/logout.html'


class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'myapp/stock_form.html'
    # success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.valid = True
        return super(StockCreateView, self).form_valid(form)


class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = "myapp/stock_detail.html"
    context_object_name = "Stock"