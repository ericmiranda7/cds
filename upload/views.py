from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadCriminalForm
from django.views import View
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

@method_decorator(login_required, name='dispatch')
class UploadView(SuccessMessageMixin, CreateView):
    template_name = 'upload/upload_form.html'
    form_class = UploadCriminalForm
    success_url = 'success/'
    success_message = 'Thank you for uploading. One of our administrators will review the FIR as soon as possible.'

""" class UploadView(View):
    def get(self, request):
        form = UploadCriminalForm()
        return render(request, 'upload/upload_form.html', {'uploadForm': form})

    def post(self, request):
        form = UploadCriminalForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            new_upload = form.save()
            return redirect('upload:upload')
        return render(request, 'upload/upload_form.html', {'uploadForm': form}) """

