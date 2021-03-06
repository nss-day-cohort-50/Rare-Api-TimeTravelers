# Generated by Django 3.2.9 on 2021-11-17 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rarerestapi', '0003_auto_20211117_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.rareusers'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.posts'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.rareusers'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='follower_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='rarerestapi.rareusers'),
        ),
    ]
