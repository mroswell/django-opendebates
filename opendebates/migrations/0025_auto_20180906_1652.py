# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opendebates', '0024_submission_happened'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'ordering': ['-happened']},
        ),
        migrations.AddField(
            model_name='submission',
            name='is_positive',
            field=models.BooleanField(default=False),
        ),
    ]
