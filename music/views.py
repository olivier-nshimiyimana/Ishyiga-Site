from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from .form import ImageThumbnailForm


def home(request):
    return render(request, 'home.html',{'name':'Bond'})


def addition(request):
    
    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    answer = number1 + number2
    return render(request, 'results.html',{'result':answer})

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