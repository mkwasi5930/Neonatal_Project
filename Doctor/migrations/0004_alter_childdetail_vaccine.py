# Generated by Django 3.2.15 on 2022-10-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_alter_childdetail_vaccine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childdetail',
            name='vaccine',
            field=models.CharField(choices=[('1', 'Vaccine_1'), ('2', 'Polio 2,Pentavalent $ Rotarix'), ('3', 'Flue Vaccine $ Vitamin A'), ('4', 'Flue Vaccine'), ('5', 'MMR $ Yellow fever'), ('6', 'Menangoccal $ Y conjugate'), ('7', 'Hepatitis A $ Dewormer'), ('8', 'Menangaccal $ MMR')], max_length=30),
        ),
    ]