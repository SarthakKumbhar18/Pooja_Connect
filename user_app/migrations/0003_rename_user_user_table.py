# Generated by Django 5.1.4 on 2025-03-13 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_user_email_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='User_table',
        ),
    ]
