from django import forms

from .models import Corrida, Motorista


class CorridaForm(forms.ModelForm):

    class Meta:
        """ meta data of form """
        model = Corrida
        fields = ['motorista', "passageiro", "total"]

    def __init__(self, *args, **kwargs):
        super(CorridaForm, self).__init__(*args, **kwargs)
        self.fields['motorista'].queryset = Motorista.objects.filter(active=True)
