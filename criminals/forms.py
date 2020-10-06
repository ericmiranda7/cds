from django import forms

class AdvancedSearch(forms.Form):
    name = forms.CharField(max_length=30, required=False)
    state = forms.CharField(max_length=12, required=False)
    city = forms.CharField(max_length=12, required=False)

    def __init__(self, *args, **kwargs):
        super(AdvancedSearch, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'