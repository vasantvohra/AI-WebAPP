from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from .models import Waste
from .models import Waste_dataset
from prediction import *
# Create your views here.

flag=False
def index(request):
    print("inside index of waste segregation")
    if request.method == 'POST':
        flag=True
        #image1 = request.FILES['image']
        name = request.FILES.get('image', False)
        if name == False:
            image1=request.POST.get('ck2')

            print(image1)
            #waste = Waste(image=image1)
            #waste.save()
            category, predicted_class, probability = predict(r'./mainapp/static/waste_sample/{}'.format(image1))
            # value load from image check box

        else:
            image1=name

            #waste = Waste(image=image1)
            #waste.save()
            waste_dataset = Waste_dataset(image=image1)
            waste_dataset.save()
            category, predicted_class, probability = predict(r'./media/waste/{}'.format(image1))
            fetched_waste = Waste_dataset.objects.get(id=waste_dataset.id)
            fetched_waste.predicted_category = predicted_class
            fetched_waste.save()
            print('waste =' ,fetched_waste.predicted_category)

        #waste_datasets = Waste_dataset.objects.all()
        #print(waste_datasets)
        return render(request, 'waste_seg/index.html',
                      {'category': category, 'predicted_class': predicted_class, 'probability': probability,
                       'flag': flag, 'fetched_waste':fetched_waste})



    else:
        flag=False
        return render(request, 'waste_seg/index.html',{'flag':flag})





def answer(request, id ):

    answer = request.POST.get('answer')
    print(id)
    fetched_obj = Waste_dataset.objects.get(id = id)
    fetched_obj.actual_category=answer
    fetched_obj.save()
    print('fetched object = ',fetched_obj)
    #image1 = request.FILES.get('image', False)
    print(answer)
    #print(image1)
    #waste = Waste(image=image1)
    #waste.save()
    #return HttpResponse('success')
    return redirect('/')



# def upload(request):
#
#     #image = request.FILES['image']
#     image1 = request.FILES['image']
#     # ./media/waste/{}.format(image)
#     print(image1)
#     #image=str(image)
#     #print(image)
#     #print(type(image))
#     waste = Waste(image=image1)
#     waste.save()
#     result = predict(r'./media/waste/{}'.format(image1))
#     print(result)
#     flag=True
#     return render(request,'waste_seg/index.html',{'result':result,'flag':flag})
#     #return HttpResponse('upload')