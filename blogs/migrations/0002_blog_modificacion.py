# Generated by Django 2.1.3 on 2018-11-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
