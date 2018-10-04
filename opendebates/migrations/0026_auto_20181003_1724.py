# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opendebates', '0025_auto_20180906_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='happened',
            field=models.DateField(null=True, blank=True),
        ),
    ]
