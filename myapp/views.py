from django.shortcuts import render



from .models import pictures

def  home (request):
    images = pictures.objects.all()
    # print(images)
    context = {'images':images}

    return render(request, 'home.html', context)








