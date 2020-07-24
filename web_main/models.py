# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class County(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.TextField()
    population = models.IntegerField(blank=True, null=True)
    growth_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'County'


class Owner(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    status = models.TextField()
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'Owner'


class Land(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    county_id = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        db_column='county_id',
    )
    rating = models.IntegerField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    owner_id = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        db_column='owner_id',
    )

    class Meta:
        managed = True
        db_table = 'Land'


class LandImprovement(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    management = models.TextField()
    cost = models.IntegerField(blank=True, null=True)
    improvement = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'LandImprovement'


