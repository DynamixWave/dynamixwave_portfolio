# Generated by Django 5.1.3 on 2025-04-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_contactmodel_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='subject',
            field=models.TextField(blank=True, null=True),
        ),
    ]
