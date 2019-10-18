from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def count(request):
    user_text = request.GET['text']
    total_count = len(request.GET['text'])
    return render(request, 'count.html', {'count':total_count, 'text':user_text} )

def about(request):
	return render(request, 'about.html')
