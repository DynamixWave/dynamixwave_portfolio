# Generated by Django 5.1.3 on 2025-04-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_ourteamprogressmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='points',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
