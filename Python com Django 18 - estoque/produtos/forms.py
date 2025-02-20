from django import forms
from .models import Produto, Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nome']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nota', 'nome', 'preco', 'quantidade']
