# Generated by Django 4.0.4 on 2022-05-04 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0015_remove_appoinment_doc_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appoinment',
        ),
    ]