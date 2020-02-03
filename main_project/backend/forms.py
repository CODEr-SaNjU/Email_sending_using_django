from django import forms
class EmailForm(forms.Form):
    email = forms.EmailField(label="email")
    Verify = forms.EmailField(label="verify email",required=True)
    Designation = forms.CharField(max_length=100,required=True)
    project = forms.CharField(max_length=100,required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea)


      