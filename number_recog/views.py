from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cars
import pandas as pd
import cv2
from .ALPR import *
import matplotlib.pyplot as plt


# Create your views here.

def index(request):
    flag = False
    show = False
    if request.method == 'POST':
        modalflag = False
        flag = True
        name = request.FILES.get('image', False)
        if name == False:
            image1 = request.POST.get('ck2')
            show = True
            print(image1)
            input_image = image1
            txt = result(r'./mainapp/static/cars/{}'.format(image1))
            return render(request, 'number_recog/index.html',
                          {'flag': flag, 'txt': txt, 'show': show, 'input_image': input_image})
        else:
            user = request.user
            if user.is_authenticated:
                show = False
                image1 = name
                cars = Cars(image=image1)
                cars.save()
                input_image = image1
                txt = result(r'./media/{}'.format(cars.image.name))
                print(txt)
                return render(request, 'number_recog/index.html',
                              {'flag': flag, 'txt': txt, 'input_image': input_image, 'show': show})
            else:
                return redirect('login')

    else:
        flag = False
        show = False
        return render(request, 'number_recog/index.html')
