from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.expense_all, name='expense_all'),
    path('details/<slug:slug>/', views.expense_detail, name='expense_detail'),
    path('categories/', views.category_all, name='categories'),
    path('subcategories/', views.subcategory_all, name='subcategories'),
    path('transaction-types/', views.transaction_type_all, name='transaction_types'),
]
