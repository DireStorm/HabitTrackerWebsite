# Generated by Django 4.0.6 on 2023-01-15 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_profile_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
