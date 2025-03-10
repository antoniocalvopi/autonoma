from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Billing
from .serializers import BillingSerializer
from rest_framework.response import Response
from rest_framework import status

class CreateBillingView(generics.CreateAPIView):
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Guardamos la factura con el usuario actual
        serializer.save(user=self.request.user)


class BillingListView(generics.ListAPIView):
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo devolvemos las facturas que pertenecen al usuario autenticado
        return Billing.objects.filter(user=self.request.user)

class BillingDetailView(generics.RetrieveAPIView):
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Billing.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("No tienes permiso para ver esta factura.")
        return obj

class BillingUpdateView(generics.UpdateAPIView):
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Billing.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("No tienes permiso para actualizar esta factura.")
        return obj

class BillingDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Billing.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("No tienes permiso para eliminar esta factura.")
        return obj