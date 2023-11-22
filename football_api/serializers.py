from rest_framework import serializers

from .models import CreateNewMatch, SendMessageToEmail


class CreateMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateNewMatch
        fields = ['home_team', 'away_team', 'date', 'stadium']


class SendEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessageToEmail
        fields = '__all__'
