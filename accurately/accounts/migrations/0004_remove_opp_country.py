# Generated by Django 2.0.1 on 2020-02-04 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_opp_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opp',
            name='country',
        ),
    ]
