from django import forms

class ContactForm(forms.Form):
    Name    = forms.CharField(max_length=50,label="Ad",required=True,widget=forms.TextInput(attrs={"placeholder":"Adınız"}))
    Email   = forms.EmailField(max_length=200,label="Email",required=True,widget=forms.EmailInput(attrs={"placeholder":"E mail adresiniz"}))
    Message = forms.CharField(max_length=1000,label="Mesajınız",required=True,widget=forms.Textarea(attrs={"placeholder":"Mesajınız"}))





