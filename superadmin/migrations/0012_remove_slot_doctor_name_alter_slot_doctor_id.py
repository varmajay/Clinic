# Generated by Django 4.0.4 on 2022-05-03 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0011_appoinment_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='doctor_name',
        ),
        migrations.AlterField(
            model_name='slot',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.user'),
        ),
    ]