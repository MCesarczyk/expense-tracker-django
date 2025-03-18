from django.db import models
from django.urls import reverse
from django.db.models.query import QuerySet
from django.contrib.auth.models import User


class TransactionType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "transaction_types"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store: transaction_type_list", args=[self.slug])


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="category_covers", default='category_covers/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store: category_list", args=[self.slug])


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(
        Category, related_name="subcategory", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store: subcategory_list", args=[self.slug])


class ExpenseManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(ExpenseManager, self).get_queryset()


class Expense(models.Model):
    id = models.IntegerField(primary_key=True)
    account_number = models.CharField(max_length=255, default="PL61109010140000071219812874")
    transaction_date = models.DateField()
    accounting_date = models.DateField()
    transaction_type = models.ForeignKey(
        TransactionType, related_name="expense", on_delete=models.CASCADE
    )
    target_account = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, related_name="expense", on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        Subcategory, related_name="expense", on_delete=models.CASCADE
    )
    details = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expense_creator"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    expenses = ExpenseManager()

    class Meta:
        verbose_name_plural = "expenses"
        ordering = ("-accounting_date",)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("store: expense_detail", args=[self.id])
