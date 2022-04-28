# Generated by Django 4.0.4 on 2022-04-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patients', 'Patients')], max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('clinic_name', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], default=None, null=True)),
                ('specialty', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('profile', models.FileField(default='profile.png', upload_to='user')),
            ],
        ),
    ]
