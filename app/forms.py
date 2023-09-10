from django import forms
from .models.entrega_atividade import EntregaAtividade
from .models.atividade import Atividade
from .models.disciplina import Disciplina
from .models.curso import Curso
from .models.entrega_atividade import EntregaAtividade

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
        
    remember = forms.BooleanField(
        label = 'Remenber me',
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-label'
            }
        )
    )

class EntregaAtividadeForm(forms.ModelForm):
    class Meta:
        model = EntregaAtividade
        exclude = ['dt_entrega']
        fields = ['resposta', 'status', 'nota', 'aluno', 
                  'atividade', 'professor', 'dt_entrega',
                  'observacao', 'file']
        
    

        labels = {
            'resposta':'Resposta',
            'status':'Status',
            'nota':'Nota',
            'aluno':'Aluno',
            'atividade':'Atividade',
            'professor':'Professor',
            'dt_entrega':'Data de Entrega',
            'observacao':'Observação',
            'file':'Arquivo'
        }

        widgets = {
            'resposta':forms.Textarea(attrs={'placeholder':'Resposta', 'cols':'50', 'rows':'10'})
        }





class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuario',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Usuario',
                'class':'form-control',
                'usuario':'usuario'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Senha',
                'class':'form-control',
                'password':'password'
            }
        )
    )


