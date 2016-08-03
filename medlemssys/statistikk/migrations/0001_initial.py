# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medlem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LokallagStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veke', models.CharField(max_length=7, verbose_name='\xc5r-veke')),
                ('n_teljande', models.IntegerField(verbose_name='tal p\xe5 teljande')),
                ('n_interessante', models.IntegerField(verbose_name='tal p\xe5 interessante')),
                ('n_ikkje_utmelde', models.IntegerField(verbose_name='tal p\xe5 ikkje utmelde')),
                ('n_totalt', models.IntegerField(verbose_name='tal p\xe5 medlemar registrert')),
                ('teljande', models.TextField(verbose_name='liste over teljande')),
                ('interessante', models.TextField(verbose_name='liste over interessante')),
                ('oppretta', models.DateTimeField(auto_now_add=True, verbose_name='oppretta')),
                ('lokallag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medlem.Lokallag')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='lokallagstat',
            unique_together=set([('lokallag', 'veke')]),
        ),
    ]