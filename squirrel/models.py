from django.db import models

class squirrel(models.Model):
    x = models.DecimalField(max_digits=1007,decimal_places=12,default=None,blank=True)
    y = models.DecimalField(max_digits=1006,decimal_places=12,default=None,blank=True)
    unique_squirrel_id = models.CharField(max_length=14,default=None,blank=True,primary_key=True)
    hectare = models.CharField(max_length=3,default=None,blank=True)
    AM = 'AM'
    PM = 'AM'
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
            )
    shift = models.CharField(max_length=2,choices=SHIFT_CHOICES,default=AM,blank=True)
    date = models.CharField(max_length=20,default=0,blank=True)
    hectare_squirrel_number = models.IntegerField(default=0,blank=True)
    age = models.CharField(max_length=8,default=None,blank=True)
    primary_fur_color = models.CharField(max_length=8,default=None,blank=True)
    highlight_fur_color = models.CharField(max_length=100,default=None,blank=True)
    combination_of_primary_and_highlight_color = models.CharField(max_length=100,default=None,blank=True)
    color_notes = models.CharField(max_length=100,default=None,blank=True)
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = (
            (GROUND_PLANE, 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            )
    location = models.CharField(max_length=100,choices=LOCATION_CHOICES,default=GROUND_PLANE,blank=True)
    above_ground_sighter_measurement = models.CharField(max_length=10,default=None,blank=True)
    specific_location = models.CharField(max_length=100,default=None,blank=True)
    running = models.BooleanField(default=None,blank=True)
    chasing = models.BooleanField(default=None,blank=True)
    climbing = models.BooleanField(default=None,blank=True)
    eating = models.BooleanField(default=None,blank=True)
    foraging = models.BooleanField(default=None,blank=True)
    other_activities = models.CharField(max_length=100,default=None,blank=True)
    kuks = models.BooleanField(default=None,blank=True)
    quaas = models.BooleanField(default=None,blank=True)
    moans = models.BooleanField(default=None,blank=True)
    tail_flags = models.BooleanField(default=None,blank=True)
    tail_twitches = models.BooleanField(default=None,blank=True)
    approaches = models.BooleanField(default=None,blank=True)
    indifferent = models.BooleanField(default=None,blank=True)
    runs_from = models.BooleanField(default=None,blank=True)
    other_interactions = models.CharField(max_length=100,default=None,blank=True)
    lat_long = models.CharField(max_length=100,default=None,blank=True)
    zip_codes = models.CharField(max_length=100,default=None,blank=True)
    community_districts = models.IntegerField(default=None,blank=True)
    borough_boundaries = models.IntegerField(default=None,blank=True)
    city_coucil_districts = models.IntegerField(default=None,blank=True)
    police_precincts = models.IntegerField(default=None,blank=True)
# Create your models here.
