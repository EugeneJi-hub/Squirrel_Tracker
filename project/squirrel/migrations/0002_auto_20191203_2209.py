# Generated by Django 3.0 on 2019-12-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='highlight_fur_color',
            field=models.CharField(blank=True, default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(blank=True, default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='x',
            field=models.DecimalField(blank=True, decimal_places=10, default=None, max_digits=1007),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='y',
            field=models.DecimalField(blank=True, decimal_places=10, default=None, max_digits=1006),
        ),
    ]
