# from django.shortcuts import render
from django.http import HttpResponse

def myIndex(request):
    # my_name = request.GET.get('name','CGU')
    my_name = request.POST.get('name','CGU')
    return HttpResponse("Hello "+my_name)# Create your views here.
