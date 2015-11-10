# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime

def add_time_to_date(apps, schema_editor):
    datetables = apps.get_model("product", "Product")
    delta = datetime.timedelta(hours=1)
    for x in datetables.objects.all():
        x.created_at = x.created_at + delta
        x.modified_at = x.modified_at + delta
        x.save()

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20151110_0026'),
    ]

    operations = [
        migrations.RunPython(add_time_to_date),
    ]
