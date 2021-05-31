from typing import Text
from django.shortcuts import render
from basicapp import forms
from .models import form_db

# Create your views here.


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        
        if form.is_valid():
            print("VALIDATION SUCCESS ")
            print("NAME : " + form.cleaned_data['name'])
            print("EMAIL : " + form.cleaned_data['email'])
            print("TEXT : " + form.cleaned_data['text'])
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')
            form_dbs = form_db(name = name, email = email, text = text)
            form_dbs.save()
            print("the data has been written to the db")
    return render(request, 'basicapp/form_page.html', {'form':form})

#, {'form_dbs':form_dbs}    