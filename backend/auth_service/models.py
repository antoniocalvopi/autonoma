from django.db import models

class BlacklistedToken(models.Model):
    # Puedes agregar un campo que almacene el token en lugar de la relación con OutstandingToken
    token = models.CharField(max_length=500)  # Guarda el token como una cadena de texto
    created_at = models.DateTimeField(auto_now_add=True)  # Un campo de fecha de creación para el registro

    def __str__(self):
        return self.token

