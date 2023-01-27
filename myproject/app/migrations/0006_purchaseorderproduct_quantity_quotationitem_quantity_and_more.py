# Generated by Django 4.1.4 on 2023-01-26 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_purchaseorderproduct_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorderproduct',
            name='quantity',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='quotationitem',
            name='quantity',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='staffID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.staff'),
        ),
    ]