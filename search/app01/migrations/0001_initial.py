# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(to='app01.ArticleType'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='app01.Category'),
        ),
    ]
