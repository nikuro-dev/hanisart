from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    return HttpResponse("hello world this is first page")

def contact_page(request):
    return HttpResponse("this is contact us page")

def about_us(request):
    return HttpResponse("this is about us page")
