from dataclasses import fields
from django import forms
from .models import Person

class  PersonalInformation(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"