# Generated by Django 5.0.1 on 2024-03-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('verified_at', models.DateTimeField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'permissions': [('can_ban_user', 'Can ban users')],
            },
        ),
    ]