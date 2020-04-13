from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
# from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Sign_verification_forged
from .models import Sign_verification_genuine
from signature_verification import *


# Create your views here.

def index(request):
    return render(request, 'mainapp/index2.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = auth.authenticate(username=username, password=password)  # this will do authentication
        if user is not None:
            auth.login(request, user)  # this will login user if user object passed by authenticate() is not null
            return redirect('/')  # call to home page
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'mainapp/login.html')


def about(request):
    return render(request, 'mainapp/about.html')


def sign_verify(request):
    flag = False
    if request.method == 'POST':
        flag = True
        genuine_sign = request.POST.get('ck2')
        forged_sign = request.FILES['forged_sign']
        sign_verification_forged = Sign_verification_forged(image=forged_sign)
        sign_verification_forged.save()
        print(sign_verification_forged.image.name)
        thresh, diff, result = main(r'./mainapp/static/genuine_signs/{}'.format(genuine_sign),
                                    r'./media/{}'.format(sign_verification_forged.image.name))
        print(thresh, diff, result)

        return render(request, 'mainapp/sign_verification.html',
                      {'thresh': thresh, 'diff': diff, 'result': result, 'flag': flag})
    else:
        flag = False
        return render(request, 'mainapp/sign_verification.html', {'flag': flag})


def signature_verification(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        return render(request, 'mainapp/signature_verification.html')
    else:
        return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('/')
