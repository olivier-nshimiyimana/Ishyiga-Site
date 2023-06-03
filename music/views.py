from django.shortcuts import render
from django.http import HttpResponse
# from django.urls import reverse
# Create your views here.
# from .form import ImageThumbnailForm

def event(request):
    return render(request, 'event',{'name':'event'})
def home(request):
    return render(request, 'home.html',{'name':'home'})
def client(request):
    return render(request, 'clients.html',{'name':'client'})


def products(request):
   return render(request, 'how.html',{'name':'products'})  

# def imageThumbnail(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         ifoto = request.FILES['image']
#         user = request.user
#         ifoto = imageThumbnail.objects.create(user=user, title=title, description=description, ifoto=image_file)
      
#         imageThumbnail.save();
#         print('Image inserted')
#         return redirect('/')
        
#     else:
#         return render(request, '#')