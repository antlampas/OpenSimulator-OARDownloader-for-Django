from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from django.contrib.auth.models import User

from pathlib import Path

from .models import *

# DOWNLOADS_DIR = "/var/opensimulator/backups/OARs/osgrid"

try:
    DOWNLOADS_DIR = Setting.objects.get(option="download_directory").value
except:
    DOWNLOADS_DIR = ""

@login_required
def index(request):
    filesList = []
    if DOWNLOADS_DIR != "":
        p = Path(DOWNLOADS_DIR)
        filesToCheck = [x for x in p.iterdir()]
        for file in filesToCheck:
            regions = AvatarRegionAssociation.objects.filter(username=Avatar.objects.get(username=User.objects.get(username=request.user.username)))
            for region in regions:
                if region.region.name in str(file.stem):
                    try:
                        with open(file) as f: pass
                        filesList.append([str(file.stem),str(region.region.simulator.grid)])
                    except IOError:
                        pass
        filesList.sort()
    context = { 'Files' : filesList }
    return render(request,'OARDownloader/index.html',context)
