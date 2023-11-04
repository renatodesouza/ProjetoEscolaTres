from django import forms
from .models.entrega_atividade import EntregaAtividade
from .models.atividade import Atividade
from .models.disciplina import Disciplina
from .models.curso import Curso
from .models.entrega_atividade import EntregaAtividade
from .models.coordenador import Coordenador
from .models.professor import Professor
from .models.aluno import Aluno
from .models.mensagem import Mensagem



PERIODO_CHOICES = [
        ('MATUTINO', 'Matutino'),
        ('NOTURNO', 'Noturno'),
]
    
MODALIDADE_CHOICES = [
    ('PRESENCIAL','PRESENCIAL'),
    ('ONLINE', 'ONLINE')
]


class EntregaAtividadeForm(forms.ModelForm):
    professores = Professor.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance._state.adding and not self.instance.aluno.has_perm('app.alterar_nota'):
            self.fields['nota'].disabled = True

    class Meta:
        model = EntregaAtividade
        fields = '__all__'

    resposta = forms.CharField(
        label = 'Resposta',
        max_length=500,

        widget=forms.Textarea(
            attrs={
                'resposta':'resposta',
            }
        )
    )

    professor = forms.ModelChoiceField(
        queryset=professores,
        empty_label='Selecione um professor',
        label='Professor',
        required=True,
        widget=forms.Select(
            attrs={
                'class':'form-control',
                'professor':'professor',
                'data-value':'professor.id'

            }
        )
    )

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

#-------------CURSO FORM------------------------------
class CursoForm(forms.ModelForm):
    coordenadores = Coordenador.objects.all()

    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'coordenador', 'periodo', 'modalidade', 'imagem']

    nome = forms.CharField(
        label = 'Nome',
        max_length = 200,
        required = True,

        widget=forms.TextInput(
            attrs={
                'placeholder':'Curso',
                'nome':'nome',
                'class':'form-control'
            }
        )
    )

    descricao = forms.CharField(
        label = 'Descrciao',
        max_length=500,
        required=True,
        
        widget=forms.Textarea(
            attrs={
                'placeholder':'Descricao do curso',
                'descricao':'descricao',
                'class':'form-control',
                'cols':'1',
                'rows':'10'
            }
        )
    )

    coordenador = forms.ModelChoiceField(
        queryset=coordenadores,
        empty_label='Selecione um coordenador',
        label = 'Coordenador',
        required = True,
        widget=forms.Select(
            attrs={
                'class':'dropdown-item coordenador-item',
                'coordenador':'coordenador',
                'id':'coordenador-input'
            }
        )
    )

    periodo = forms.ChoiceField(
        choices=PERIODO_CHOICES,
        widget=forms.SelectMultiple(
            attrs={
                'class':'dropdown-item periodo-item',
                
                'id':'periodo-input'
            }
        )
    )

    modalidade = forms.ChoiceField(
        choices=MODALIDADE_CHOICES,
        widget=forms.SelectMultiple(
            attrs={
                'class':'dropdown-item modalidade-item',
                
                'id':'modalidade-input'
            }
        )
    )
    

    imagem = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'class':'form-label',
                'accept': 'image/*',
                'imagem':'imagem'
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



class MensagemForm(forms.ModelForm):
    aluno = Aluno.objects.all()
    professor = Professor.objects.all()

    class Meta:
        model = Mensagem
        fields = ['remetente', 'destinatario', 'assunto', 'mensagem']

    