# Generated by Django 4.1.5 on 2023-03-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(db_index=True, max_length=20, unique=True)),
                ('descriptive_name', models.CharField(max_length=50)),
                ('first_open_date', models.DateField()),
                ('instrument_type', models.CharField(choices=[('ST', 'Stock'), ('FT', 'Futures'), ('OT', 'Options'), ('IX', 'Index'), ('CU', 'Currency'), ('CF', 'Currency Futures'), ('CO', 'Currency Options'), ('IF', 'Index Futures'), ('IO', 'Index Options')], default='ST', max_length=2)),
            ],
            options={
                'verbose_name': 'Instrument',
                'verbose_name_plural': 'Instruments',
            },
        ),
    ]
