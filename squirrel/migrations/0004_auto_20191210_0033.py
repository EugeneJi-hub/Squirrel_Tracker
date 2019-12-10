# Generated by Django 3.0 on 2019-12-10 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0003_auto_20191204_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='unique_squirrel_id',
            new_name='Unique_Squirrel_ID',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='above_ground_sighter_measurement',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='age',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='approaches',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='borough_boundaries',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='chasing',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='city_coucil_districts',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='climbing',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='color_notes',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='combination_of_primary_and_highlight_color',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='community_districts',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='eating',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='foraging',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='hectare',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='hectare_squirrel_number',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='highlight_fur_color',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='indifferent',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='kuks',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='lat_long',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='location',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='moans',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='other_activities',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='other_interactions',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='police_precincts',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='primary_fur_color',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='quaas',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='running',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='runs_from',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='shift',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='specific_location',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='tail_flags',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='tail_twitches',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='x',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='y',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='zip_codes',
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Latitude',
            field=models.DecimalField(blank=True, decimal_places=13, default=None, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Longitude',
            field=models.DecimalField(blank=True, decimal_places=13, default=None, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Other_Activities',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], default=None, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Runs_from',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Shift',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Specific_Location',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Tail_flags',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Tail_twitches',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]