from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage
from django.conf import settings
from  . forms import EmailForm
from django.conf import settings

class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'html_files/Sender.html'

    def get(self,request,*args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{'email_form':form})
    
    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            email   = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            option = form.cleaned_data['option']
            files = request.FILES.getlist('attach')
            try:
                mail = EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
                for f in files:
                    mail.attach(f.name,f.read(),f.content_type)
                    mail.send()
                return render(request,self.template_name,{'email_form':form,'error_message':'sent Email to %s'%email})
            except:
                return render(request,self.template_name,{'email_form':form,'error_message':'Either the attachment is too big or corrupt '})
        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})             

