# Generated by Django 3.2.9 on 2021-11-17 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rarerestapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='user_id',
            new_name='user',
        ),
    ]
