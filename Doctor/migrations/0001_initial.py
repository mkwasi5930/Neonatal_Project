# Generated by Django 3.2.15 on 2022-10-03 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('firstname', models.CharField(default='mc', max_length=30, primary_key=True, serialize=False)),
                ('lastname', models.CharField(default='moto', max_length=30)),
                ('email', models.EmailField(default='abedtati1@gmail.com', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mother',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('nationalId', models.IntegerField(default='12345678')),
                ('email', models.EmailField(default='abedtati1@gmail.com', max_length=30)),
                ('age', models.IntegerField()),
                ('numberOfKids', models.IntegerField(default='1')),
                ('maritalstatus', models.CharField(choices=[('S', 'Single'), ('M', 'Married')], default='1', max_length=30)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='mutuma', max_length=30)),
                ('lname', models.CharField(default='moffat', max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=30)),
                ('weight', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(default='mc', on_delete=django.db.models.deletion.CASCADE, to='Doctor.doctor')),
            ],
        ),
    ]
