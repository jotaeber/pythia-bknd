# Generated by Django 5.0 on 2023-12-05 01:06

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
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('course', models.CharField(max_length=50)),
                ('ssn', models.DecimalField(max_digits=10, decimal_places=0)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
