# Generated by Django 4.0.2 on 2022-03-25 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_leave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_subject',
            name='subject_status',
        ),
    ]
