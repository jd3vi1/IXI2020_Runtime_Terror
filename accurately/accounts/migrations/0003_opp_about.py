# Generated by Django 2.0.1 on 2020-02-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_opp_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='opp',
            name='about',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]