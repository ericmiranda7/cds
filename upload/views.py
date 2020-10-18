from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadCriminalForm
from django.views import View
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import sqlite3, os
from sqlite3 import Error
from criminals.models import VerifiedCriminal

class UploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'upload/upload_form.html'
    form_class = UploadCriminalForm
    success_url = 'success/'
    success_message = 'Thank you for uploading. One of our administrators will review the FIR as soon as possible.'

    def check_copsdb(self, criminal):
        conn = None
        my_fir_no = criminal.fir_no
        print(my_fir_no)
        my_name = criminal.name
        try:
            conn = sqlite3.connect('copsdb.sqlite3')
            cursor = conn.cursor()
            cursor.execute(f'SELECT name FROM Criminal WHERE fir_no = {my_fir_no}')
            name = cursor.fetchone()
            print(type(name))
            print(type(my_name))
            if name and name[0] == my_name:
                VerifiedCriminal.objects.create(name=criminal.name, age=criminal.age, physical_description=criminal.physical_description, date=criminal.date, crime_type=criminal.crime_type, arresting_agency=criminal.arresting_agency, photo=criminal.photo, status=criminal.status, fir_photo=criminal.fir_photo, fir_no=criminal.fir_no, state=criminal.state, city=criminal.city, rating=2)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.check_copsdb(self.object)
        return super().form_valid(form)