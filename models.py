#Author: antlampas
#Date: 2023-04-23
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django.db import models

from django.contrib.auth.models import User

class Setting(models.Model):
    option = models.CharField(max_length=26)
    value  = models.CharField(max_length=256)
    models.UniqueConstraint(fields=['option'],name='unique_option')
    def __str__(self):
        return self.option + " = " + self.value
    def __unicode__(self):
        return self.option + " = " + self.value