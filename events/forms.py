from django import forms
from .models import Event, Comment
from .models import Cadastro

class EventForm(forms.ModelForm):
    """Formulário utilizado para a inserção de novos eventos."""
    class Meta:
        model = Event
        fields = ['date', 'event', 'priority',]

class CommentForm(forms.ModelForm):
    """Formulário usado para a inserção de comentários em um evento."""
    class Meta:
        model = Comment
        fields = ['text', 'author', 'email', 'event']

class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ['nome', 'idade', 'cor', 'sexo', 'cidade', 'Nacionalidade', 'etinia']