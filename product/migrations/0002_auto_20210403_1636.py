# Generated by Django 3.1.7 on 2021-04-03 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
