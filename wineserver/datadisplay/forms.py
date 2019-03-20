from django import forms


class filterform(forms.Form):
    filter =  forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)
    sortcheck = forms.BooleanField()

class loginform(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)