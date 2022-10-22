# Generated by Django 3.2.15 on 2022-10-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Childdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=30)),
                ('middle_Name', models.CharField(max_length=30)),
                ('last_Name', models.CharField(max_length=30, null=True)),
                ('mothers_Name', models.CharField(max_length=30)),
                ('fathers_Name', models.CharField(max_length=30, null=True)),
                ('weight', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=30)),
                ('temperature', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('vaccine', models.CharField(max_length=30)),
            ],
        ),
    ]
