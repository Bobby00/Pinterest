from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from . models import Image,Location,Category

# Create your views here.
def index(request):
    images= Image.objects.all()

    return render(request, 'index.html',{"images":images})

def details(request,id):
    try:
        specific = Image.objects.get(id=id)
    except DoesNotExist:
        raise Http404()
    
    return render(request, "details.html",{"specific":specific})

# def full_image(request, id):
#     try:
#         full_image = Image.objects.get(id=id)
#     except DoesNotExist:
#         raise Http404()
    
#     return render(request, "image.html",{"full_image":full_image})
    
