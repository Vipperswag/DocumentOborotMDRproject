from django.shortcuts import HttpResponse
from django.shortcuts import render
# Create your views here.
def glavnaya(request):
    return HttpResponse('А робит или нет?')
def neglavnaya(request):
    return render(request, 'index.html')