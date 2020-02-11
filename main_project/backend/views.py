from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage , EmailMultiAlternatives
from django.conf import settings
from  . forms import EmailForm
from django.conf import settings
from django.template.loader import get_template,render_to_string
from backend.utils import render_to_pdf
from .models import EmailData

class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'html_files/Home.htm'

    def get(self,request,*args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{'email_form':form})
    
    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            to  = form.cleaned_data['email']
            Designation = form.cleaned_data['Designation']
            project = form.cleaned_data['project']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            verify = form.cleaned_data['verify']
            context = {
                'to':to,
                'Designation':Designation,
                'project':project,
                'subject':subject,
                'message':message,
                }
            html_template = get_template('html_files/confirm.htm')
            html_Content = html_template.render(context)
            try:
                msg = EmailMultiAlternatives(subject,html_Content,settings.EMAIL_HOST_USER,[verify])
                msg.attach_alternative(html_Content,"text/html")
                # msg.attach_alternative(pdf,"application/pdf")
                msg.send()
                return HttpResponse('Please confirm your email address to complete the registration')
                # return render(request,self.template_name,{'email_form':form,'error_message':'sent Email to %s'%email})
            except:
                return render(request,self.template_name,{'email_form':form,})
        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})             
