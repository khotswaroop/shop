# Generated by Django 4.1.3 on 2023-01-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
