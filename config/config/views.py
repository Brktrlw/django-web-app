from django.shortcuts import render
from USERS.forms import ContactForm

def v_homePage(request):
    contactform = ContactForm(data=request.POST or None)
    if contactform.is_valid():
        name   = contactform.cleaned_data.get('Name')
        Email  = contactform.cleaned_data.get('Email')
        Message= contactform.cleaned_data.get('Message')
        return render(request,"homePage.html",context={"contactform": contactform})

    return render(request,"homePage.html",context={"contactform": contactform})




