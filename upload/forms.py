from django import forms
from .models import UploadCriminal, States, Cities

class UploadCriminalForm(forms.ModelForm):
    class Meta:
        model = UploadCriminal
        fields = ['name', 'age', 'physical_description', 'date',
        'state', 'city', 'crime_type', 'arresting_agency', 'photo']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter your name", 'class': 'form-control'}),
            'age': forms.TextInput(attrs={'placeholder': "Enter Criminal's age", 'class': 'form-control'}),
            'physical_description': forms.TextInput(attrs={'placeholder': 'Enter physical description of criminal', 'type': 'textarea', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'state': forms.Select(attrs={'name': 'state', 'id': 'id_state', 'class': 'form-control'}),
            'city': forms.Select(attrs={'id': 'id_city', 'class': 'form-control chained-fk', 'name': 'city', 'data-chainfield': 'state', 'data-url': '/chaining/filter/upload/Cities/state/upload/UploadCriminal/city', 'data-value': 'null', 'data-auto_choose': 'true', 'data-empty_label': 'Select City'}),
            'crime_type': forms.Select(attrs={'placeholder': 'Type of Crime', 'class': 'form-control'}),
            'arresting_agency': forms.TextInput(attrs={'placeholder': 'Arresting Agency', 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*', 'name': 'photo', 'class': 'form-control', 'style': 'border: none;', 'id': 'id_photo'})
        }