# Generated by Django 5.0.9 on 2024-09-17 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nurse_app', '0002_alter_nurse_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]