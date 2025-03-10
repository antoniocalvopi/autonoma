from django.urls import path
from .views import BudgetListCreateView, BudgetDetailView

urlpatterns = [
    path('lists/', BudgetListCreateView.as_view(), name='budget-list-create'), 
    path('lists/<int:budget_id>/', BudgetDetailView.as_view(), name='budget-detail'),  
]