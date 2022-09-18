# Generated by Django 4.1 on 2022-09-17 11:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='url',
            name='id',
        ),
        migrations.RemoveField(
            model_name='url',
            name='uuid',
        ),
        migrations.AddField(
            model_name='url',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='url',
            name='expires_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='url',
            name='short_id',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='url',
            name='link',
            field=models.CharField(max_length=2048),
        ),
        migrations.AddField(
            model_name='url',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shortner.user'),
        ),
    ]
