from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView


# Create your views here.
class ContactView(SuccessMessageMixin, CreateView):
    template_name = 'contactus/contact.html'
    form_class = ContactForm
    success_url = 'success/'
    success_message = "Submitted, Thank You !"