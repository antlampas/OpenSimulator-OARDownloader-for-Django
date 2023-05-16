#Author: antlampas
#Date: 2023-04-23
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from pathlib import Path

from django.apps import apps
from django.contrib.auth.models import User
#TODO: there's a better way to do this for sure...
if apps.is_installed("OpenSimBaseInterface"):
    from OpenSimBaseInterface.models import *

from .models import *

#There's a dependency between this app and the OpenSimBaseInterface app
#TODO: find a good and elegant way to implement this constrain...
#So far, this code is too weak and prone to bugs...

#TODO: reinforce decouple between this app and the actual OARs provider

try:
    DOWNLOADS_DIR = Setting.objects.get(option="download_directory").value
except:
    DOWNLOADS_DIR = ""

@login_required
def index(request):
    if apps.is_installed("OpenSimBaseInterface"):
        filesList = []
        if DOWNLOADS_DIR != "":
            p = Path(DOWNLOADS_DIR)
            filesToCheck = [x for x in p.iterdir()]
            for file in filesToCheck:
                regions = OwnerRegionAssociation.objects.filter(username=Avatar.objects.get(username=User.objects.get(username=request.user.username)))
                for region in regions:
                    if region.region.name in str(file.stem):
                        try:
                            with open(file) as f: pass
                            filesList.append([str(file.stem),str(region.region.simulator.grid)])
                        except IOError:
                            pass
            filesList.sort()
        else:
            fileList.append(["OARSDOWNLOADDIRECTORYMISSING","OARs download directory not set"])
    else:
        fileList.append(["OPENSIMBASEINTERFACE_NOT_FOUND","OpenSimuBaseInterface not found"])
    context = { 'Files' : filesList }
    return render(request,'OARDownloader/index.html',context)
