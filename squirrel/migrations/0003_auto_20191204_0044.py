# Generated by Django 3.0 on 2019-12-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0002_auto_20191203_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='highlight_fur_color',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='x',
            field=models.DecimalField(blank=True, decimal_places=13, default=None, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='y',
            field=models.DecimalField(blank=True, decimal_places=13, default=None, max_digits=1000),
        ),
    ]
