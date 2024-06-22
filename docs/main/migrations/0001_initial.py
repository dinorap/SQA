# Generated by Django 4.2.2 on 2023-06-09 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_number', models.BigIntegerField(null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_number', models.BigIntegerField(max_length=13, null=True, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('status', models.TextField(choices=[('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('Pending', 'Pending')])),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consump_amount', models.FloatField(default=1, null=True)),
                ('penalty_amount', models.FloatField(default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_consumption', models.BigIntegerField(null=True)),
                ('status', models.TextField(choices=[('Paid', 'Paid'), ('Pending', 'Pending')], null=True)),
                ('duedate', models.DateField(null=True)),
                ('penaltydate', models.DateField(null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]
