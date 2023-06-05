# Generated by Django 4.1.9 on 2023-06-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "algo_trading",
            "0023_orderhistory_orderhistory_order_history_status_idx_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="exchange_order_id",
            field=models.BigIntegerField(
                blank=True, default=None, null=True, verbose_name="exchange order id"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_id",
            field=models.BigIntegerField(
                blank=True, default=None, null=True, verbose_name="zerodha order id"
            ),
        ),
    ]
