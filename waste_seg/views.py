from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from .models import Waste
from .models import Waste_dataset
from .prediction import *

# Create your views here.

flag = False


def index(request):
    user = request.user
    if user.is_authenticated:
        print("inside index of waste segregation")
        if request.method == 'POST':
            flag = True
            show = False
            name = request.FILES.get('image', False)
            if name == False:
                image1 = request.POST.get('ck2')
                show = True
                print(image1)
                category, predicted_class, probability = predict(r'./mainapp/static/waste_sample/{}'.format(image1))
                return render(request, 'waste_seg/index.html',
                              {'category': category, 'predicted_class': predicted_class, 'probability': probability,
                               'flag': flag, 'show': show})

            else:
                image1 = name
                show = False
                waste_dataset = Waste_dataset(image=image1)
                waste_dataset.save()
                category, predicted_class, probability = predict(r'./media/{}'.format(waste_dataset.image.name))
                fetched_waste = Waste_dataset.objects.get(id=waste_dataset.id)
                fetched_waste.predicted_category = predicted_class
                fetched_waste.save()
                print('waste =', fetched_waste.predicted_category)
                return render(request, 'waste_seg/index.html',
                              {'category': category, 'predicted_class': predicted_class, 'probability': probability,
                               'flag': flag, 'fetched_waste': fetched_waste, 'show': show})

        else:
            flag = False
            show = False
            return render(request, 'waste_seg/index.html', {'flag': flag, 'show': show})
    else:
        return redirect('login')

def answer(request, id):
    answer = request.POST.get('answer')
    print(id)
    fetched_obj = Waste_dataset.objects.get(id=id)
    fetched_obj.actual_category = answer
    fetched_obj.save()
    print('fetched object = ', fetched_obj)
    print(answer)
    return redirect('index')
