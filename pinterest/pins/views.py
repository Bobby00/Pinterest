from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from . models import Image,Location,Category

# Create your views here.
def index(request):
    images= Image.objects.all()

    return render(request, 'index.html',{"images":images})

def details(request, image_id):
    try:
        specific = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    
    return render(request, "details.html",{"specific":specific})
