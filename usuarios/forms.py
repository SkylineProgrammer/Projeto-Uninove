from django import forms
from .models import Perfil

class PerfilFotoForm(forms.ModelForm):
    """Formulário simplificado para o upload de foto de perfil."""
    class Meta:
        model = Perfil
        fields = ['foto_perfil']
        # Usando widget para poder estilizar melhor no HTML
        widgets = {
            'foto_perfil': forms.FileInput(attrs={'id': 'id_foto_perfil', 'style': 'display: none;'})
        }