# Generated by Django 3.0.7 on 2020-08-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customizer', '0016_auto_20200721_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapobject',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapobject',
            name='frequency_text',
            field=models.CharField(default='Never', max_length=20),
        ),
    ]