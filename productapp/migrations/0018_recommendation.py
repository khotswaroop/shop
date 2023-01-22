# Generated by Django 4.1.3 on 2023-01-21 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0017_delete_recommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='productapp.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='productapp.usermodel')),
            ],
        ),
    ]