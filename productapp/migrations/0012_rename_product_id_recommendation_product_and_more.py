# Generated by Django 4.1.3 on 2023-01-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0011_alter_usermodel_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='recommendation',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
