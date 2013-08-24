from django import forms
from models import Person
from django.forms import ModelForm


class AddPersonForm(ModelForm):
    b_date = forms.DateField()
    about = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'b_date',
                  'photography', 'email', 'jabber', 'about', )
