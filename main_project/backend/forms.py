from django import forms
class EmailForm(forms.Form):
    CHOICES=(
        ("1","Yes"),
        ("2","No"),
    )
    email = forms.EmailField()
    subject = forms.CharField(max_length=100, required=True)
    option = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect(attrs={'name':'option'}),label='If you want send a file')
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'id':'option'}),required=True)
    message = forms.CharField(widget=forms.Textarea)


      