# Generated by Django 3.2.4 on 2021-08-03 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_scheduledmail_send_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledmail',
            name='send_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 6, 55, 35, 544663, tzinfo=utc)),
        ),
    ]