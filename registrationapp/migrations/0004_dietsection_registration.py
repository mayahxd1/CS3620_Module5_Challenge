# Generated by Django 5.0.5 on 2024-05-26 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0003_alter_registration_event_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietsection',
            name='registration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registrationapp.registration'),
        ),
    ]
