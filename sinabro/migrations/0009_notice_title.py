# Generated by Django 2.1.1 on 2018-10-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinabro', '0008_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='title',
            field=models.CharField(blank=True, max_length=30, verbose_name='제목'),
        ),
    ]
