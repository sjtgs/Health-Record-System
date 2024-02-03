# Generated by Django 5.0.1 on 2024-02-02 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor_app', '0003_delete_appointment'),
        ('patient_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField()),
                ('purpose_review', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.patient')),
            ],
        ),
    ]