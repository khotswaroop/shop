# Generated by Django 4.1.3 on 2023-01-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0010_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]