# Generated by Django 5.0.5 on 2024-06-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='display_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]