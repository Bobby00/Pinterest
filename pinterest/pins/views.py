from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from . models import Image,Location,Category
# from django.db.models import Q

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
def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message, "categories":searched_categories})

    else:
        message ="You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

