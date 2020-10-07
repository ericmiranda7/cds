from django.shortcuts import render
from django.core.paginator import Paginator
from .models import VerifiedCriminal
from .forms import AdvancedSearch
from django.views import View
from django.views.generic import DetailView, ListView
from upload.models import States, Cities


class CriminalsView(ListView):
    template_name = 'criminals/criminals.html'
    form_class = AdvancedSearch
    model = VerifiedCriminal
    paginate_by = 6
    context_object_name = 'criminals'

    def get_queryset(self):
        name = self.kwargs.get('name', None)
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return self.model.objects.filter(name__contains=form.cleaned_data['name']) \
                .filter(state__name__contains=form.cleaned_data['state']) \
                .filter(city__name__contains=form.cleaned_data['city'])
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CriminalsView, self).get_context_data(**kwargs)
        context['advancedSearch'] = AdvancedSearch()
        context['states'] = States.objects.all()
        context['cities'] = Cities.objects.all()
        return context


class CriminalDetailView(DetailView):
    model = VerifiedCriminal
    template_name = 'criminals/criminal_detail.html'
    context_object_name = 'criminal'
