# Generated by Django 4.0.4 on 2022-06-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
