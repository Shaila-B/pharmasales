from django.urls import path

from . import views
from .views import GetDrugReviewViewSet, GetPharmaSalesViewSet

urlpatterns = [
    path('read_csv_for_database/', views.read_csv, name='read_csv_for_database'),
    path('sales_of_drug_classification/', GetPharmaSalesViewSet.as_view(), name="sales_of_drug_classification"),
    path('drug_reviews/', GetDrugReviewViewSet.as_view(), name="drug_reviews"),
]