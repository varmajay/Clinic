# Generated by Django 4.0.4 on 2022-04-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='doctor_id',
            field=models.CharField(default=None, max_length=10),
        ),
    ]