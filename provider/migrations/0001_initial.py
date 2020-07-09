# Generated by Django 3.0.8 on 2020-07-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=254)),
                ('pincode', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=75)),
                ('phone', models.CharField(max_length=10)),
                ('service_type', models.CharField(max_length=10)),
                ('base_price', models.PositiveIntegerField()),
                ('rate_per_km', models.PositiveIntegerField(default=0)),
                ('delete_status', models.BooleanField(default=False)),
            ],
        ),
    ]