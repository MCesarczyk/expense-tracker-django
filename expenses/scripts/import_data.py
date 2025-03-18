import pandas as pd
from django.contrib.auth.models import User
from ..models import Category, Subcategory, Expense, TransactionType

# Read CSV file into a DataFrame
# csv_file_path = "expenses/FIXTURE.csv"

def run(*args):
    csv_file_path = args[0]
    print(f"Importing data from {csv_file_path}")
    df = pd.read_csv(
        csv_file_path,
        na_values=[""],
        dtype={
            "Numer rachunku/karty": str,
            "Data transakcji": str,
            "Data rozliczenia": str,
            "Rodzaj transakcji": str,
            "Na konto/Z konta": str,
            "Odbiorca/Zleceniodawca": str,
            "Opis": str,
            "Obciążenia": float,
            "Uznania": float,
            "Saldo": float,
            "Kategoria": str,
            "Podkategoria": str,
            "Szczegóły": str,
        },
    )

    df.fillna({"Obciążenia": 0}, inplace=True)
    df.fillna({"Uznania": 0}, inplace=True)
    df.fillna("N/A", inplace=True)

    # Iterate through the DataFrame and create model instances
    for index, row in df.iterrows():
        # Create or get transaction type instance
        transaction = row["Rodzaj transakcji"]
        if type(transaction) == str and not transaction == "N/A":
            ftransaction = transaction.lower().replace(" ", "-")
            ttype, created = TransactionType.objects.get_or_create(
                name=transaction,
                defaults={"slug": ftransaction},
            )

        # Create or get the Category instance
        cat = row["Kategoria"]
        if type(cat) == str and not cat == "N/A":
            fcat = cat.lower().replace(" ", "-")
            category, created = Category.objects.get_or_create(
                name=cat, defaults={"slug": fcat}
            )

        # # Create or get the Subcategory instance
        subcat = row["Podkategoria"]
        if type(subcat) == str and not subcat == "N/A":
            fsubcat = subcat.lower().replace(" ", "-")
            subcategory, created = Subcategory.objects.get_or_create(
                name=subcat, category=category, defaults={"slug": fsubcat}
            )

        duty = row["Obciążenia"]
        credit = row["Uznania"]
        if duty:
            amount = duty
        elif credit:
            amount = credit
        else:
            amount = 0

        # Create the Expense instance
        expense = Expense(
            account_number=row["Numer rachunku/karty"],
            transaction_date=row["Data transakcji"],
            accounting_date=row["Data rozliczenia"],
            transaction_type=ttype,
            target_account=row["Na konto/Z konta"],
            target=row["Odbiorca/Zleceniodawca"],
            description=row["Opis"],
            amount=amount,
            category=category,
            subcategory=subcategory,
            details=row["Szczegóły"],
            created_by=User.objects.first(),  # Set the appropriate user here
        )
        # to save the current product
        expense.save()

    print("CSV data has been loaded into the Django database.")
