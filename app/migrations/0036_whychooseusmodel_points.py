# Generated by Django 5.1.3 on 2025-04-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_aboutmodel_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='whychooseusmodel',
            name='points',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
