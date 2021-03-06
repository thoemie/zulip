# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-12 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0219_toggle_realm_digest_emails_enabled_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='audible_notifications',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='desktop_notifications',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email_notifications',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='push_notifications',
            field=models.NullBooleanField(default=None),
        ),
    ]
