# Generated by Django 2.2.5 on 2019-09-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordEvent',
            fields=[
                ('active', models.BooleanField()),
                ('audio_start_time', models.IntegerField()),
                ('guid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
