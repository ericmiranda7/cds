from os import stat
from django import forms
from upload.models import States, Cities
from django.urls import reverse_lazy
# Clever selects
from clever_selects.form_fields import ChainedChoiceField, ChainedModelChoiceField
from clever_selects.forms import ChainedChoicesForm


class AdvancedSearch(forms.Form):
    name = forms.CharField(max_length=30, required=False)
    state = forms.ModelChoiceField(States.objects.all(), required=False, blank=True, empty_label="Select state")
    city = ChainedModelChoiceField(parent_field='state', ajax_url=reverse_lazy('criminals:ajax_chained_view'), model=Cities, required=False,
        empty_label="Select city"
    )
    crime = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search by crime'}))

    def __init__(self, *args, **kwargs):
        super(AdvancedSearch, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
