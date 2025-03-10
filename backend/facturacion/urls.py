from django.urls import path
from .views import CreateBillingView, BillingListView, BillingDetailView, BillingUpdateView, BillingDeleteView
urlpatterns = [
    path('bills/', CreateBillingView.as_view(), name='create-billing'),
    path('bills/', BillingListView.as_view(), name='billing-list'),
    path('bills/<int:id>/', BillingDetailView.as_view(), name='billing-detail'),
    path('bills/<int:id>/edit/', BillingUpdateView.as_view(), name='billing-update'),
    path('bills/<int:id>/delete/', BillingDeleteView.as_view(), name='billing-delete'),
]