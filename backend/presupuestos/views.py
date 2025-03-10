from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .models import Budget
from .serializers import BudgetSerializer


class BudgetListCreateView(APIView):
    """View to list and create budgets."""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Get a list of all budgets for the authenticated user."""
        budgets = Budget.objects.filter(user=request.user)  # Usamos request.user directamente
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new budget for the authenticated user."""
        data = request.data
        data['user'] = request.user.id  # Asigna el usuario autenticado directamente

        # Serializamos y validamos los datos
        serializer = BudgetSerializer(data=data, context={'request': request})  # Pasar el contexto
        if serializer.is_valid():
            serializer.save()  # Guarda el presupuesto con el usuario asignado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BudgetDetailView(APIView):
    """View to retrieve, update, or delete a specific budget."""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, budget_id, user):
        """Helper method to get the budget for a given user and budget_id."""
        try:
            budget = Budget.objects.get(id=budget_id, user=user)
            return budget
        except Budget.DoesNotExist:
            return None

    def get(self, request, budget_id):
        """Retrieve a specific budget."""
        budget = self.get_object(budget_id, request.user)
        if budget is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, budget_id):
        """Update a specific budget."""
        budget = self.get_object(budget_id, request.user)
        if budget is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        # Actualizamos el presupuesto con los datos recibidos
        data = request.data
        serializer = BudgetSerializer(budget, data=data, partial=True, context={'request': request})  # partial=True permite la actualización parcial

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, budget_id):
        """Delete a specific budget."""
        budget = self.get_object(budget_id, request.user)
        if budget is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        budget.delete()
        return Response({"detail": "Budget deleted successfully."}, status=status.HTTP_204_NO_CONTENT)