from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import os
from django.core.exceptions import ValidationError

from .models import Video

# comment these two imports and uncomment import on line 17
#from VideoDetection import *
#from ImageDetection import *

from ImageVideoDetection1 import *
import os


# Create your views here.
def index(request):
    flag = False
    videoflag = False
    imageflag = False
    sampleflag = False
    if request.method == 'POST':
        flag = True
        video1 = request.FILES.get('video', False)
        # video1 = request.FILES['video']
        if video1 == False:
            # sample image is selected
            sampleflag = True
            videoflag = False
            imageflag = False
            imagename = request.POST.get('ck2')
            input_name = imagename
            truck = request.POST.get('truck')
            person = request.POST.get('person')
            bus = request.POST.get('bus')
            bicycle = request.POST.get('bicycle')
            bird = request.POST.get('bird')
            motorcycle = request.POST.get('motorcycle')
            probability = request.POST.get('probability')
            if probability == None:
                probability = 30
            objects = {'truck': bool(truck), 'person': bool(person), 'bus': bool(bus), 'bicycle': bool(bicycle),
                       'bird': bool(bird),
                       'motorcycle': bool(motorcycle)}
            none = False
            for key, value in objects.items():
                if value == True:
                    none = True
                    break
            if none == True:
                out_str, out_name = ImageDetection(r'./mainapp/static/sample_object/{}'.format(imagename), objects, int(probability))
            else:
                out_str, out_name = ImageDetection(r'./mainapp/static/sample_object/{}'.format(imagename), None,int(probability))
            output_string = out_str
            output_name = out_name
            return render(request, 'object_det/index.html',
                          {'flag': flag, 'input_name': input_name, 'objects': objects, 'videoflag': videoflag,
                           'imageflag': imageflag, 'output_string': output_string, 'output_name': output_name,
                           'sampleflag': sampleflag})
        else:
            ext = os.path.splitext(video1.name)[1]
            valid_extensions = ['.mp4']
            if ext.lower() in valid_extensions:
                sampleflag = False
                videoflag = True
                imageflag = False
                input_name = video1
                truck = request.POST.get('truck')
                person = request.POST.get('person')
                bus = request.POST.get('bus')
                bicycle = request.POST.get('bicycle')
                bird = request.POST.get('bird')
                motorcycle = request.POST.get('motorcycle')
                probability = request.POST.get('probability')
                if probability == None:
                    probability = 30
                print(truck, person, bus, bicycle, bird, motorcycle)
                video = Video(videofile=video1)
                video.save()
                objects = {'truck': bool(truck), 'person': bool(person), 'bus': bool(bus), 'bicycle': bool(bicycle),
                           'bird': bool(bird),
                           'motorcycle': bool(motorcycle)}
                none = False
                for key, value in objects.items():
                    if value == True:
                        none = True
                        break
                if none == True:
                    out_path = VideoDetection(r'./media/{}'.format(video.videofile.name), objects,int(probability))
                else:
                    out_path = VideoDetection(r'./media/{}'.format(video.videofile.name),None,int(probability))
                output_name = os.path.basename(out_path)
                return render(request, 'object_det/index.html',
                              {'flag': flag, 'input_name': input_name, 'output_name': output_name, 'objects': objects,
                               'videoflag': videoflag, 'imageflag': imageflag, 'sampleflag': sampleflag})
            else:
                sampleflag = False
                videoflag = False
                imageflag = True
                input_name = video1
                truck = request.POST.get('truck')
                person = request.POST.get('person')
                bus = request.POST.get('bus')
                bicycle = request.POST.get('bicycle')
                bird = request.POST.get('bird')
                motorcycle = request.POST.get('motorcycle')
                probability = request.POST.get('probability')
                if probability == None:
                    probability = 30
                print(truck, person, bus, bicycle, bird, motorcycle)
                video = Video(videofile=video1)
                video.save()
                objects = {'truck': bool(truck), 'person': bool(person), 'bus': bool(bus), 'bicycle': bool(bicycle),
                           'bird': bool(bird),
                           'motorcycle': bool(motorcycle)}
                none = True
                for key, value in objects.items():
                    if value == True:
                        none = False
                        break
                if none == False:
                    out_str, out_name = ImageDetection(r'./media/{}'.format(video.videofile.name), objects,int(probability))
                else:
                    out_str, out_name = ImageDetection(r'./media/{}'.format(video.videofile.name), None,int(probability))
                output_string = out_str
                output_name = out_name
                return render(request, 'object_det/index.html',
                              {'flag': flag, 'input_name': input_name, 'objects': objects, 'videoflag': videoflag,
                               'imageflag': imageflag, 'output_string': output_string, 'output_name': output_name,
                               'sampleflag': sampleflag})


    else:
        sampleflag = False
        flag = False
        videoflag = False
        imageflag = False
        return render(request, 'object_det/index.html', {'flag': flag})
