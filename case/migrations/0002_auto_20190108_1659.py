# Generated by Django 2.1.4 on 2019-01-08 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='case.Category'),
        ),
        migrations.AlterField(
            model_name='case',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='case.Company'),
        ),
    ]
