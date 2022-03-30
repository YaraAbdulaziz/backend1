# Generated by Django 3.2.6 on 2022-03-30 07:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Please Enter Correct Name', regex='[A-Za-z]')])),
                ('pr_description', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='account.store')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sz_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_type', models.CharField(choices=[('None', 'None'), ('Size', 'size'), ('Color', 'color'), ('Size-Color', 'size-color')], default='None', max_length=40)),
                ('pr_price', models.DecimalField(decimal_places=2, max_digits=1000, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.RegexValidator(message='Enter Correct Price', regex='^[0-9]*$')])),
                ('pr_qunatity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.RegexValidator(message='Enter Correct Value', regex='^[0-9]*$')])),
                ('in_stock', models.BooleanField(default=False)),
                ('pr_img', models.ImageField(upload_to='product/')),
                ('pr_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='product.color')),
                ('pr_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size', to='product.size')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='product.product')),
            ],
        ),
    ]