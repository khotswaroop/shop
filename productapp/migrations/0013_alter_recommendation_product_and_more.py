# Generated by Django 4.1.3 on 2023-01-21 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0012_rename_product_id_recommendation_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.product'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.usermodel'),
        ),
    ]
