# Generated by Django 5.1.6 on 2025-03-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_alter_transactiontype_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_covers'),
        ),
    ]
