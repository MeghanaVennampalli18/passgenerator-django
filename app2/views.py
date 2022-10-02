from unicodedata import name
from django.shortcuts import HttpResponse,render
import random
  
def generatepasswd(request):
    
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special Characters'):
        characters.extend(list('!@#$%^&*(){}[]'))  
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))      

    length=int(request.GET.get('length'))
    thepass=""
    for x in range(length):
        thepass+=random.choice(characters)
    return render(request, 'generator/password.html',{'password': thepass})
def home(request):
    return render(request, 'generator/home.html')  
def about(request):
    return render(request,'generator/about.html')     

# Create your views here.
