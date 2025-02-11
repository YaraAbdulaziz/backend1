# Generated by Django 4.0.3 on 2022-04-11 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_name', models.CharField(max_length=50)),
                ('ev_host', models.CharField(max_length=15)),
                ('ev_description', models.CharField(max_length=150)),
                ('ev_img', models.ImageField(upload_to='event/')),
            ],
        ),
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_type', models.CharField(choices=[('Price', ' Price'), ('Free', 'Free')], default='Free', max_length=10)),
                ('ev_price', models.IntegerField(default=0)),
                ('ev_date', models.DateField()),
                ('ev_duration', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ev_detail', to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_location_name', models.CharField(max_length=50)),
                ('ev_lon', models.FloatField()),
                ('ev_lat', models.FloatField()),
                ('event_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_location', to='event.eventdetail')),
            ],
        ),
    ]
