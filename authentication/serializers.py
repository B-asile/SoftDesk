from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Serialization de l'objet du profil utilisateur"""

    class Meta:
        model = models.User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        """define exception for API function with password"""
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """fonction de validation_data <<passe par dessus le modèle>>"""
        user = models.User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Géstion de la mise à jour du compte utilisateur"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)



