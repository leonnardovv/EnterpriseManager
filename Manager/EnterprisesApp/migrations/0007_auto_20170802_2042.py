# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EnterprisesApp', '0006_auto_20170802_1951'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enterprises',
            new_name='Enterprise',
        ),
    ]
