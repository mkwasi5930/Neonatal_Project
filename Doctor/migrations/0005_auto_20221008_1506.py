# Generated by Django 3.2.15 on 2022-10-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0004_alter_childdetail_vaccine'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='moffa', max_length=30)),
                ('lastname', models.CharField(default='mutuma', max_length=30)),
                ('email', models.EmailField(default='mc123@gmail', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MotherInfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('nationalId', models.IntegerField(default='12345678')),
                ('email', models.EmailField(default='abedtati1@gmail.com', max_length=30)),
                ('age', models.IntegerField()),
                ('numberOfKids', models.IntegerField(default='1')),
                ('maritalstatus', models.CharField(choices=[('S', 'Single'), ('M', 'Married')], default='1', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='mother',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Mother',
        ),
    ]
