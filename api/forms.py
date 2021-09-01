from django import forms
from.models import ScheduledMail

class MailForm(forms.ModelForm):
    class Meta:
        model = ScheduledMail
        exclude  = ['sender',]

        widgets = {
                'subject': forms.TextInput(attrs={
                    'class': 'form-control',
                    'max-length': '70',
                    }),
                'body': forms.Textarea(attrs={
                    'class': 'form-control',
                    'max-length': '40000',
                    }),
                'recipients_list': forms.EmailInput(attrs={
                    'class': 'form-control',
                    }),
                'send_on': forms.DateTimeInput(attrs={
                    'class': 'input-group date form-control ',
                    }),
                'attachment_file': forms.FileInput(attrs={
                    'class': 'form-control',

                    }),

                }
