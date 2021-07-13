# Generated by Django 3.1.5 on 2021-05-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_setting_about2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('testimos', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]