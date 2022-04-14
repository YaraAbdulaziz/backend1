# Generated by Django 4.0.3 on 2022-04-11 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drb_name', models.CharField(max_length=50)),
                ('drb_host', models.CharField(max_length=15)),
                ('drb_description', models.CharField(max_length=150)),
                ('drb_img', models.ImageField(upload_to='drb/')),
            ],
        ),
        migrations.CreateModel(
            name='DrbDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drb_type', models.CharField(choices=[('Price', ' Price'), ('Free', 'Free')], default='Free', max_length=10)),
                ('drb_price', models.IntegerField(default=0)),
                ('drb_date', models.DateField()),
                ('drb_duration', models.DateTimeField()),
                ('drb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drb_detail', to='drb.drb')),
            ],
        ),
        migrations.CreateModel(
            name='DrbLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drb_location_name', models.CharField(max_length=50)),
                ('drb_lon', models.FloatField()),
                ('drb_lat', models.FloatField()),
                ('drb_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drb_location', to='drb.drbdetail')),
            ],
        ),
    ]