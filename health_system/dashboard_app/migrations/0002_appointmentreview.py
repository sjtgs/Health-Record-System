# Generated by Django 5.0.3 on 2024-05-09 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0001_initial'),
        ('doctor_app', '0001_initial'),
        ('nurse_app', '0002_alter_nurse_email'),
        ('patient_app', '0002_remove_patient_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('purpose', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_app.doctor')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse_app.nurse')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.patient')),
            ],
        ),
    ]