# Generated by Django 4.1.4 on 2023-01-27 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_quotation_qtyprovided_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='vendorID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.vendor'),
        ),
    ]