# Generated by Django 4.2.11 on 2024-05-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
