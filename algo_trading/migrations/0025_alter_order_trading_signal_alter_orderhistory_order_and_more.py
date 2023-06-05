# Generated by Django 4.1.9 on 2023-06-05 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("algo_trading", "0024_alter_order_exchange_order_id_alter_order_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="trading_signal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trading_signal",
                to="algo_trading.tradingsignal",
            ),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_history",
                to="algo_trading.order",
            ),
        ),
        migrations.AlterField(
            model_name="tradingsignal",
            name="instrument",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trading_signal",
                to="algo_trading.instrument",
            ),
        ),
    ]
