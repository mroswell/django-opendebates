# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('opendebates', '0023_sitemode_announcement_page_regex'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='happened',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
