from django import forms
from .models import AvaliacaoFilme


class AvaliacaoFilmeForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoFilme
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.5}),
            'comentario': forms.Textarea(attrs={'rows': 4}),
        }
