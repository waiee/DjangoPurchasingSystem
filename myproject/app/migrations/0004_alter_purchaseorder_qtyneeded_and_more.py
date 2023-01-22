# Generated by Django 4.1.4 on 2023-01-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_purchaseorderproduct_productname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='qtyNeeded',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='qtyProvided',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='totalPrice',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='qtyProvided',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='quotationStatus',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='totalPrice',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='itemName',
            field=models.TextField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='itemPriceperUnit',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='quantity',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendorAddress',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendorContact',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendorName',
            field=models.TextField(max_length=20, null=True),
        ),
    ]