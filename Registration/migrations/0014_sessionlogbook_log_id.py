# Generated by Django 3.2.6 on 2021-09-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0013_auto_20210919_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionlogbook',
            name='log_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
