# Generated by Django 5.0.7 on 2024-11-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='four_digit_auth_key',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]