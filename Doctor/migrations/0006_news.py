# Generated by Django 3.2.15 on 2022-11-01 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0005_auto_20221008_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('about', models.CharField(max_length=15)),
                ('Description', models.CharField(max_length=10000)),
            ],
        ),
    ]
