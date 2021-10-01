# Generated by Django 3.2.7 on 2021-10-01 18:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveSmallIntegerField(default=0, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('english_sentence', models.TextField()),
                ('highlight_word', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('chinese_translation', models.TextField(blank=True, null=True)),
                ('original_source', models.URLField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('publish_date', models.DateField(default=datetime.date.today)),
                ('is_understand', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='words_in_sentences.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
