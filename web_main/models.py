# This is an auto-generated Django model module.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class County(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    pop2018 = models.IntegerField()
    growthrate = models.FloatField(db_column='GrowthRate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'county'


class Owner(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'owner'


class Land(models.Model):
    id = models.IntegerField(primary_key=True)
    county_id = models.ForeignKey(
        County,
        on_delete = models.CASCADE,
        db_column = 'county_id',
        to_field  = 'id',
    )
    rating = models.SmallIntegerField()
    area = models.IntegerField()
    owner_id = models.ForeignKey(
        Owner,
        on_delete = models.CASCADE,
        db_column = 'owner_id',
        to_field  = 'id',
    )

    class Meta:
        managed = False
        db_table = 'land'


class LandImprovement(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    management = models.CharField(max_length=50)
    cost = models.FloatField()
    improvement = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'land_improvement'


class LandDetails(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    county_id = models.ForeignKey(
        County,
        on_delete = models.DO_NOTHING,
        db_column = 'county_id',
        to_field  = 'id',
    )
    rating = models.SmallIntegerField()
    area = models.IntegerField()
    owner_id = models.ForeignKey(
        Owner,
        on_delete = models.DO_NOTHING,
        db_column = 'owner_id',
        to_field  = 'id',
    )
    owner_name = models.CharField(max_length=50)
    owner_status = models.CharField(max_length=50)
    county_name = models.CharField(max_length=50)
    county_pop = models.IntegerField()
    county_growth_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'vLandDetails'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


