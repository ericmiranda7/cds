from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadCriminalForm
from django.views import View
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class UploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'upload/upload_form.html'
    form_class = UploadCriminalForm
    success_url = 'success/'
    success_message = 'Thank you for uploading. One of our administrators will review the FIR as soon as possible.'