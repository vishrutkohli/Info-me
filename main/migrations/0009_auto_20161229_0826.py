# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20161228_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisations',
            name='description',
            field=models.CharField(default=b'NULL', max_length=1050),
        ),
        migrations.AlterField(
            model_name='organisations',
            name='img1',
            field=models.CharField(default=b'NULL', max_length=1050),
        ),
        migrations.AlterField(
            model_name='organisations',
            name='img2',
            field=models.CharField(default=b'NULL', max_length=1050),
        ),
        migrations.AlterField(
            model_name='organisations',
            name='img3',
            field=models.CharField(default=b'NULL', max_length=1050),
        ),
        migrations.AlterField(
            model_name='organisations',
            name='name',
            field=models.CharField(default=b'NULL', max_length=1050),
        ),
    ]
