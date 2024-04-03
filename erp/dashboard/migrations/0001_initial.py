# Generated by Django 5.0.3 on 2024-03-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cliente', models.CharField(max_length=150)),
                ('Barrio', models.CharField(max_length=120)),
                ('Localidad', models.CharField(max_length=120)),
                ('Fecha_de_compra', models.DateField()),
                ('Valor_compra', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
