from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .signature_extraction import *
from .signature_filter import *
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# Create your views here.

def index(request):
    print("inside index of signature extraction")
    user = request.user
    if user.is_authenticated:
        flag = False
        if request.method == 'POST':
            if request.POST.get('form') == 'form1':
                pg = 1
            elif request.POST.get('form') == 'form2':
                pg = 2
            elif request.POST.get('form') == 'form3':
                pg = 3

            canny = request.POST.get('Canny')
            if canny=='2':
                form1(pg,0,1)
                main(pg)
                print("filter",canny)
            elif canny=='None':
                canny=0
                form1(pg)
            elif canny=='1':
                form1(pg,int(canny))
            else:
                form1(pg)
            flag = True
            return render(request, 'signature_ver/index1.html', {'pg': pg, 'flag': flag})
        else:
            flag = False
            return render(request, 'signature_ver/index1.html', {'flag': flag})

    else:
        return redirect('login')
