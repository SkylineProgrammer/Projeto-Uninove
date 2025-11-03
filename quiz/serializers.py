from rest_framework import serializers
from .models import Pergunta, Resposta 
from.models import Pergunta, Resposta, Pontuacao 

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ['id', 'texto'] 
        #Nunca expor 'is_correta' aqui

class PerguntaSerializer(serializers.ModelSerializer):
    # Serializa todas as respostas relacionadas as pergunta do quiz
    respostas = RespostaSerializer(many=True, read_only=True) 

    class Meta:
        model = Pergunta
        fields = ['id', 'texto', 'tempo_limite', 'respostas']
 
 


# classe para registrar a pontuaçao / mapear as rotas das perguntas 

class PontuacaoSerializer(serializers.ModelSerializer):
    """
    Serializer para o histórico de pontuações.
    """
    # Mapeia a dificuldade 'F', 'M', 'D' para o nome completo (Fácil, Médio, Difícil)
    dificuldade_nome = serializers.CharField(source='get_dificuldade_display', read_only=True) 

    class Meta:
        model = Pontuacao
        fields = ['id', 'pontos_totais', 'dificuldade', 'dificuldade_nome', 'data_conclusao']
        read_only_fields = fields