# Generated by Django 5.0.1 on 2024-01-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
