#from msilib.schema import Error
from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField(min_length=5,  max_length=60)
    height = forms.IntegerField()
    age = forms.IntegerField()

    def clean_full_name(self):
        fullname = self.cleaned_data['full_name']
        if not fullname.istitle():
            raise forms.ValidationError('Error')
        return fullname
    
    def clean_height(self):
        height = self.cleaned_data['height']
        if (height < 70) or (height > 250):
            raise forms.ValidationError('Error')
        return height

    def clean_age(self):
        age = self.cleaned_data['age']
        if (age < 14) or (age > 99):
            raise forms.ValidationError('Error')
        return age

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if (len(gender) > 1) :
            raise forms.ValidationError('Error')
        return gender