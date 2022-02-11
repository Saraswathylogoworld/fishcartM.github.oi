# Generated by Django 4.0 on 2022-01-21 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webFishapp', '0008_fwcart_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('cartid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webFishapp.fwcart')),
            ],
        ),
    ]
