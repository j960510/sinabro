# Generated by Django 2.1.1 on 2018-10-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinabro', '0006_auto_20181015_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.TextField(blank=True),
        ),
    ]
