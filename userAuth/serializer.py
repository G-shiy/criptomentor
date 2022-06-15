from rest_framework import serializers
from userAuth.models import Text, Usuario
from userAuth import validators
from datetime import datetime

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha",
        error_messages= {"blank": "o campo senha não pode ficar vazio"}
    )
    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha",
        error_messages={"blank": "o campo de confirmação de senha não pode ficar vazio"},
    )
    is_staff = serializers.BooleanField(
        label="Membro da Equipe",
        help_text="Indica que usuário consegue acessar o site de administração.",
        default=False
    )
    is_superuser = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente.",
        default=False,
        
    )

    class Meta:
        model = Usuario
        fields = ['id','email','username', 'password','password_confirm', 'tel','data_nascimento', 'cpf', 'pfp', 'created_at','premium', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {
                'write_only': True,
                },
            'email': {
                'error_messages': {"blank": "o campo email não pode ficar vazio"}
                },
            'cpf': {
                'error_messages': {"blank": "o campo cpf não pode ficar vazio"}
                },
            'username': {
                'error_messages': {"blank": "o campo usuario não pode ficar vazio"}
                },
        
        }
 
    def validate(self, data: dict):
        if not validators.username_valido(data['username']):
            raise serializers.ValidationError({"Usuário contém caractéres além de A-Z:" "Usuário contém caractéres além de A-Z"})
        if not validators.cpf_valido(data['cpf']):
            raise serializers.ValidationError({"Cpf inválido:" "Cpf inválido"})
        if not validators.tel_valido(data['tel']):
            raise serializers.ValidationError({"Telefone inválido": "Telefone inválido"})
        return data

    def save(self):
        conta = Usuario(
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
            cpf=self.validated_data['cpf'],
            pfp=self.validated_data['pfp'],
            tel=self.validated_data['tel'],
            data_nascimento=self.validated_data['data_nascimento'],
            created_at=self.validated_data['created_at'],
            )

        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError(
                {'password': 'As senhas não são iguais.'}
            )

        if len(password) < 5:
            raise serializers.ValidationError(
                {'password': 'A senha é curta demais'}
            )

        conta.set_password(password)
        conta.save()

        return conta
        

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = Usuario
        fields = ['username', 'password']


"""
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AnaliseSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Analise
        fields = '__all__'"""

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'
