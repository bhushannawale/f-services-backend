# Generated by Django 3.0.8 on 2020-07-08 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consumer', '0001_initial'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('amount', models.PositiveIntegerField()),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='consumer.Consumer')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='provider.Provider')),
            ],
        ),
    ]
