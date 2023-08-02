from django import forms

from info.models import ClientModel


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        exclude = ['created_at']
