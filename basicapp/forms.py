from django import forms
from django.core import validators
#from .models import form_db

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    #crf hidden for security ex to ensure input dont going to another website
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    #ins = form_db(name = name, email = email, text = text)
    #ins.save()
   # print("the data has been written to the db")                             
"""
#we can do it loke validator= like up in botcatcher
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT!')
        return botcatcher
"""
