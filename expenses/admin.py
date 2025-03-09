from django.contrib import admin
from .models import Category, Expense, Subcategory, TransactionType


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "created_at", "updated_at"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        "description",
        "transaction_date",
        "accounting_date",
        "transaction_type",
        "category",
    ]
    search_fields = ["title"]
    prepopulated_fields = {"id": ("description",)}
