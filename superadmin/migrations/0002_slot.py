# Generated by Django 4.0.4 on 2022-04-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('doctor_name', models.CharField(max_length=30)),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 am To 10:00 am'), (1, '10:00 am TO 11:00 am'), (2, '11:00 am To 12:00 am'), (3, '12:00 am To 01:00 pm'), (4, '02:00 pm To 03:00 pm'), (5, '03:00 pm To 04:00 pm'), (6, '04:00 pm To 05:00 pm')])),
                ('weeks', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
            ],
        ),
    ]