from django.shortcuts import render, get_object_or_404
from expenses import models


def expense_all(request):
    expenses = models.Expense.expenses.all()[:50]
    context = {"expenses": expenses}
    return render(request, "expenses/expenses_list.html", context)


def expense_detail(request, slug):
    expense = get_object_or_404(models.Expense, id=slug)
    return render(request, "expenses/expense_detail.html", {"expense": expense})


def category_all(request):
    categories = models.Category.objects.all()
    context = {"categories": categories}
    return render(request, "expenses/categories_list.html", context)


def subcategory_all(request):
    subcategories = models.Subcategory.objects.all()
    context = {"subcategories": subcategories}
    return render(request, "expenses/subcategories_list.html", context)


def transaction_type_all(request):
    transaction_types = models.TransactionType.objects.all()
    context = {"transaction_types": transaction_types}
    return render(request, "expenses/transaction_types_list.html", context)
