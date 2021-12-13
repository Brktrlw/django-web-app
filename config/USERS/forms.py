from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(max_length=50,label="Ad",required=True)
    surname = forms.CharField(max_length=50,label="Soyad",required=True)
    email   = forms.EmailField(max_length=200,label="Email",required=True)
    message = forms.CharField(max_length=1000,label="Mesajınız",required=True)





