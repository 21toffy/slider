from django.shortcuts import render



from .models import pictures

def  home (request):
    images = pictures.objects.all()
    context = {'images':images}

    return render(request, 'home.html', context)








