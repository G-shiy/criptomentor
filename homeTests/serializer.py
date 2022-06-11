from rest_framework import serializers
from models import Questions, choice
from datetime import date

class TestSerializer(serializers.ModelSerializer):
    class_test = serializers.DictField(
        question01 = serializers.CharField(
            max_length=1,
            write_only=True,
            label="Digite a pergunta",
            error_messages={"blank": "A pergunta não pode estar em branco"},
            ),
        question02 = serializers.CharField(
            max_length=1,
            write_only=True,
            label="Digite a pergunta",
            error_messages={"blank": "A pergunta não pode estar em branco"},
            ),
        question03 = serializers.CharField(
            max_length=1,
            write_only=True,
            label="Digite a pergunta",
            error_messages={"blank": "A pergunta não pode estar em branco"},
            ),
        question04 = serializers.CharField(
            max_length=1,
            write_only=True,
            label="Digite a pergunta",
            error_messages={"blank": "A pergunta não pode estar em branco"},
            ),
        question05 = serializers.CharField(
            max_length=1,
            write_only=True,
            label="Digite a pergunta",
            error_messages={"blank": "A pergunta não pode estar em branco"},
            ),
    )

    class Meta:
        model = Questions
        fields = '__all__'
        
    def save(self):
        prova = Questions(
            class_test = self.validated_data['class_test'],
            title = self.validated_data['title'],
            created_at = self.validated_data['class_test'],
            resposta = self.validated_data['class_test']
        )
        prova.save()

        return prova