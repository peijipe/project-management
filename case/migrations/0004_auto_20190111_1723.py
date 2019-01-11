# Generated by Django 2.1.4 on 2019-01-11 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_auto_20190111_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='lower_cost',
            field=models.IntegerField(blank=True, default='0', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='下限単金'),
        ),
        migrations.AlterField(
            model_name='case',
            name='member',
            field=models.IntegerField(blank=True, default='0', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='人数'),
        ),
        migrations.AlterField(
            model_name='case',
            name='number',
            field=models.IntegerField(blank=True, default='0000', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='組合案件番号'),
        ),
    ]
