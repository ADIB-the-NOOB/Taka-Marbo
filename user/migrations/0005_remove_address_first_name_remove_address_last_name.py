# Generated by Django 4.1.2 on 2022-10-30 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_address_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='address',
            name='last_name',
        ),
    ]
