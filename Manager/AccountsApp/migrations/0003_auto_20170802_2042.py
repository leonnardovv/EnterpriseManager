# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AccountsApp', '0002_auto_20170802_1952'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounts',
            new_name='Account',
        ),
    ]
