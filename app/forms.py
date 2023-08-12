from django import forms
from .models.entrega_atividade import EntregaAtividade
from .models.atividade import Atividade
from .models.disciplina import Disciplina
from .models.curso import Curso


class EntregaAtividadeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance._state.adding and not self.instance.aluno.has_perm('app.alterar_nota'):
            self.fields['nota'].disabled = True

    class Meta:
        model = EntregaAtividade
        fields = '__all__'

    def clean_campo_limitado(self):
        nota = self.cleaned_data['nota']

        return nota
    
class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor')
        super().__init__(*args, **kwargs)
        self.order_fields['disciplina'].queryset = Disciplina.objects.filter(professor=professor)


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'coordenador', 'periodo', 'modalidade', 'imagem']
        

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    password = forms.PasswordInput()
