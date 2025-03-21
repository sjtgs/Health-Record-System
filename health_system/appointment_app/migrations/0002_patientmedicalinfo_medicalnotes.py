# Generated by Django 5.0.10 on 2025-01-10 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0001_initial'),
        ('doctor_app', '0001_initial'),
        ('patient_app', '0004_ocrdata_extracted_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedicalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('blood_pressure', models.IntegerField()),
                ('hiv_status', models.CharField(choices=[('P', 'Postive'), ('N', 'Negative')], max_length=3)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_notes', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_app.doctor')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.patient')),
                ('patient_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment_app.patientmedicalinfo')),
            ],
        ),
    ]
