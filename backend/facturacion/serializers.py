from rest_framework import serializers
from .models import Billing

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['id', 'user', 'total_amount', 'description', 'status', 'due_date', 'created_at']