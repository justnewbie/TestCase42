from django import forms

from widgets import DatePickerWidget
from models import Person


class AddPersonForm(forms.ModelForm):
    b_date = forms.DateField(widget=DatePickerWidget())
    about = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'b_date',
                  'photography', 'email', 'jabber', 'about', )
