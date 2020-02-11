from django import forms
from .models import EmailData
from django.forms import ModelForm


class EmailForm(forms.ModelForm):
    email = forms.EmailField(label="email")
    verify = forms.EmailField(label="verify email",required=True)
    Designation = forms.CharField(max_length=100,required=True)
    project = forms.CharField(max_length=100,required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = EmailData
        fields = ['email','verify','Designation','project','subject','message']