from django.shortcuts import render
from USERS.forms import ContactForm

def v_homePage(request):
    contactform=ContactForm()

    return render(request,"homePage.html",context={"contactform":contactform})

