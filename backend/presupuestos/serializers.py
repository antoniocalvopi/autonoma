from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'name', 'amount', 'description', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        # Asegúrate de asignar el usuario dentro del serializador si no está siendo pasado.
        user = self.context['request'].user  # Obtén el usuario de la solicitud
        validated_data['user'] = user
        return super().create(validated_data)