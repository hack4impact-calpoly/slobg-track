# Generated by Django 2.2.6 on 2020-10-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slobg_app', '0018_auto_20200524_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
