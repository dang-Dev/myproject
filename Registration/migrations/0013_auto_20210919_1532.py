# Generated by Django 3.2.6 on 2021-09-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0012_logbook_body_temp_second_attempt'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionLogbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=100, null=True)),
                ('date_time_created', models.DateTimeField(null=True)),
                ('date_time_expired', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='logbook',
            name='remark',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
