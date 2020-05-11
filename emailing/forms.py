from django import forms
from .models import Emailing


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "semail",
        "id": "semail",
        "placeholder": "Email Address",
    }), label="")

    class Meta:
        model = Emailing
        fields = ('email', )
