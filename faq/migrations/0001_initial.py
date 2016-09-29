# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-29 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jmbo', '0003_auto_20160530_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jmbo.ModelBase')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
            bases=('jmbo.modelbase',),
        ),
    ]
