from django import forms
from models import Person
from django.forms import ModelForm


class AuthForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class Add_Person(ModelForm):
    b_date = forms.DateField()

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'b_date', 'about', 'email', 'jabber', 'photography')