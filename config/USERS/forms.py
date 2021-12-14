from django import forms

class ContactForm(forms.Form):
    Name    = forms.CharField(max_length=50,label="Ad",required=True,widget=forms.TextInput(attrs={"placeholder":"Adınız"}))
    Email   = forms.EmailField(max_length=200,label="Email",required=True,widget=forms.EmailInput(attrs={"placeholder":"E mail adresiniz"}))
    Message = forms.CharField(max_length=1000,label="Mesajınız",required=True)



    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        self.fields['Message'].widget=forms.Textarea(attrs={"placeholder":"Mesajınızı Giriniz","class":"form-control"})
        self.fields['Name'].widget=forms.TextInput(attrs={"placeholder":"Adınızı Giriniz","class":"form-control"})
        self.fields['Email'].widget=forms.TextInput(attrs={"placeholder":"Mail adresinizi Giriniz","class":"form-control"})



    def clean_Name(self):
        Name = self.cleaned_data.get("Name")
        if Name=="a":
            raise forms.ValidationError("Lütfen başka harf giriniz")
        return Name



