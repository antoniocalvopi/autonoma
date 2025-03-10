from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="Pendiente")
    due_date = models.DateField(default=date.today)  # Establecer la fecha actual como valor por defecto
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Factura {self.id} - {self.description}"