# Generated by Django 4.1.1 on 2022-12-06 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Cart',
            new_name='cart',
        ),
    ]
