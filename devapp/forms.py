from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from devapp.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
        
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['email', 'first_name', 'last_name', 'phone', 'age', 'sex', 'i_am_registering_for', 'location', 'does_your_child_have_any_experience_coding']
        