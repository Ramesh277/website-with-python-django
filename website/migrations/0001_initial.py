# Generated by Django 4.1.4 on 2023-01-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=250)),
                ('age', models.IntegerField(max_length=10)),
                ('is_Active', models.BooleanField(default=False)),
                ('mobile', models.IntegerField(max_length=10)),
            ],
        ),
    ]
