# Generated by Django 4.1 on 2022-09-18 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_next_curser_promo_next_cursor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promo',
            name='next_cursor',
        ),
    ]
