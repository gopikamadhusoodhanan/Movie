# Generated by Django 4.2.6 on 2023-12-08 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='imag',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Available',
            new_name='available',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]
