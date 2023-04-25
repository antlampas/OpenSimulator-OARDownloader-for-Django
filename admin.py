#Author: antlampas
#Date: 2023-04-23
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django.contrib import admin

from .models import Setting,Grid,Simulator,Region,Avatar,AvatarRegionAssociation

@admin.register(Setting)
class settingAdmin(admin.ModelAdmin):
    option = "option"
    value  = "value"
    list_display = ["option","value"]

@admin.register(Grid)
class gridAdmin(admin.ModelAdmin):
    name = "name"
    list_display = ["name"]

@admin.register(Simulator)
class simulatorAdmin(admin.ModelAdmin):
    name = "name"
    list_display = ["name"]

@admin.register(Region)
class regionAdmin(admin.ModelAdmin):
    name      = "name"
    simulator = "simulator"
    list_display = ["name","simulator"]

@admin.register(Avatar)
class avatarAdmin(admin.ModelAdmin):
    firstName = "firstName"
    lastName  = "lastName"
    username  = "username"
    list_display = ["username","firstName","lastName"]

@admin.register(AvatarRegionAssociation)
class avatarRegionAssociationAdmin(admin.ModelAdmin):
    username = "username"
    region   = "region"
    list_display = ["username","region"]
