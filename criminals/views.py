from django.shortcuts import render
from django.core.paginator import Paginator
from .models import VerifiedCriminal, CrimeType
from .forms import AdvancedSearch
from django.views import View
from django.views.generic import DetailView, ListView
from upload.models import States, Cities
from clever_selects.views import ChainedSelectChoicesView


class CriminalsView(ListView):
    template_name = 'criminals/criminals.html'
    form_class = AdvancedSearch
    model = VerifiedCriminal
    paginate_by = 6
    context_object_name = 'criminals'

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            if not form.cleaned_data['state']:
                form.cleaned_data['state'] = ''
            if not form.cleaned_data['city']:
                form.cleaned_data['city'] = ''
            criminals = self.model.objects.filter(name__contains=form.cleaned_data['name']) \
                .filter(state__name__contains=form.cleaned_data['state']) \
                .filter(city__name__contains=form.cleaned_data['city'])
            if form.cleaned_data['crime']:
                criminals = criminals.filter(crime_type_id__exact=int(form.cleaned_data['crime']))
            return criminals
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CriminalsView, self).get_context_data(**kwargs)
        context['advancedSearch'] = AdvancedSearch()
        context['crimes'] = CrimeType.objects.all()
        return context


class CriminalDetailView(DetailView):
    model = VerifiedCriminal
    template_name = 'criminals/criminal_detail.html'
    context_object_name = 'criminal'

class AjaxChainedView(ChainedSelectChoicesView):
    def get_child_set(self):
        return Cities.objects.filter(state_id=self.parent_value)