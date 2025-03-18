from django.shortcuts import render, get_object_or_404, redirect
from expenses import models
from .forms import CSVImportForm
from .scripts import import_data


def import_expenses(request):
    if request.method == "POST":
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["csv_file"]
            import_data.run(csv_file)
            return redirect("success_page")
    else:
        form = CSVImportForm()

    return render(request, "expenses/import_expenses.html", {"form": form})


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
