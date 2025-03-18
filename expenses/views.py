from django.shortcuts import render, get_object_or_404
from expenses import models


def expense_all(request):
    expenses = models.Expense.expenses.all()[:50]
    context = {"expenses": expenses}
    return render(request, "expenses/expenses_list.html", context)
