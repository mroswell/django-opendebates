# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opendebates', '0026_auto_20181003_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='citation',
            field=models.CharField(db_index=True, max_length=2000, null=True, verbose_name='Optional link to full proposal or reference', blank=True),
        ),
    ]
