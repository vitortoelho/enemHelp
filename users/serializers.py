from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()

# Serializer para criar um novo usuário
class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    name = serializers.CharField(required=True)  # Apenas o nome, não mais first_name e last_name

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'name')

    # Validação para garantir que as senhas coincidam
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data

    # Criação do usuário
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],  # Usando o campo name
        )
        return user

# Serializer para login (só precisa do email e senha)
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
