# Generated by Django 4.0 on 2022-01-23 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webFishapp', '0009_fcheckout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcheckout',
            old_name='name',
            new_name='fname',
        ),
    ]
