# Generated by Django 3.0.2 on 2020-06-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='extra_data',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
