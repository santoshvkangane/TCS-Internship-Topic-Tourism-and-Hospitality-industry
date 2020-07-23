from django import forms
from tourismapp.models import *


class Signup2Form(forms.ModelForm):
    class Meta:
        model = Signup2
        fields = "__all__"


class Registration2Form(forms.ModelForm):
    class Meta:
        model = Registration2
        fields = "__all__"


class EventregForm(forms.ModelForm):
    class Meta:
        model = Eventreg
        fields = ['Firstname', 'Lastname', 'EmailId', 'ename', 'Contact', 'Gender']
        # widgets = {
        #     'Gender': forms.TextInput(attrs={'placeholder': 'Male/Female'})
        # }


class MeetingregForm(forms.ModelForm):
    class Meta:
        model = Meetingreg
        fields = "__all__"


class ExhibitionregForm(forms.ModelForm):
    class Meta:
        model = Exhibitionreg
        fields = "__all__"


class FestivalregForm(forms.ModelForm):
    class Meta:
        model = Festivalreg
        fields = "__all__"


class CulturalregForm(forms.ModelForm):
    class Meta:
        model = Culturalreg
        fields = "__all__"


class EntertainmentregForm(forms.ModelForm):
    class Meta:
        model = Entertainmentreg
        fields = "__all__"


class HospitalityregForm(forms.ModelForm):
    class Meta:
        model = Hospitalityreg
        fields = "__all__"


