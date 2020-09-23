from django import forms
from .models import UploadCriminal, States, Cities


class UploadCriminalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadCriminalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UploadCriminal
        fields = ['name', 'age', 'physical_description', 'date',
                  'state', 'city', 'crime_type', 'arresting_agency', 'photo', 'fir_photo', 'fir_no']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter your name", }),
            'age': forms.TextInput(attrs={'placeholder': "Enter Criminal's age", }),
            'physical_description': forms.TextInput(attrs={'placeholder': 'Enter physical description of criminal', 'type': 'textarea', }),
            'date': forms.DateInput(attrs={'type': 'date', }),
            'crime_type': forms.Select(attrs={'placeholder': 'Type of Crime', }),
            'arresting_agency': forms.TextInput(attrs={'placeholder': 'Arresting Agency', }),
            'fir_no': forms.TextInput(attrs={'placeholder': "Enter FIR Number",}),
        }
