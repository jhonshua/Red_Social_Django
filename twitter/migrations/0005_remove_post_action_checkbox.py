# Generated by Django 5.1.4 on 2025-01-11 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_relationship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='action_checkbox',
        ),
    ]