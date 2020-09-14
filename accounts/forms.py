from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Add email field to django form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password2 = forms.CharField(
        label=("Confirm password:"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
        )
    

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # For all fields attrs
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
            self.fields[field].help_text = None

        # Specific field attrs
        self.fields['username'].widget.attrs.update({
                'title': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'})
        self.fields['email'].widget.attrs.update({
                'title': 'Enter a valid email'})
        self.fields['password1'].widget.attrs.update({
                'title': 'Your password can’t be too similar to your other personal information.\nYour password must contain at least 8 characters.\nYour password can’t be a commonly used password.\nYour password can’t be entirely numeric.'})
        self.fields['password2'].widget.attrs.update({
                'title': 'Enter the same password as before, for verification.'})


    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # For all fields attrs
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
    