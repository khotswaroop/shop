# Generated by Django 4.1.3 on 2023-01-21 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0007_alter_usermodel_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
