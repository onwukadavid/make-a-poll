# Generated by Django 5.0.1 on 2024-03-21 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='verified_at',
            field=models.DateTimeField(null=True),
        ),
    ]