# Generated by Django 4.1 on 2022-09-17 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_promo_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='notion_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promo',
            name='page_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
