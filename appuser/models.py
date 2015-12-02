import datetime

from django.db import models
from django.db.models import F

# Create your models here.

#self.refercode = "{:0>6d}".format(1)

class User(models.Model):

    name = models.CharField(blank=True, max_length=100)
    plan = models.ForeignKey("Plan")
    refercode = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

class Plan(models.Model):

    name = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return self.name


class HistoricalPlan(models.Model):

    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    owner = models.ForeignKey("User")
    actual = models.ForeignKey("Plan")

    class Meta:
        verbose_name = 'HistorialPlan'
        verbose_name_plural = 'HistorialPlans'

    def __unicode__(self):
        pass
