from django import forms

from pages.models import ReservationModel, ContactModel


class ReservationModelForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['name', 'email', 'date', 'time', 'number_of_people']


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']
