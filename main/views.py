from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html', {'message': 'Ledgers of Merit and Demerit'})

# Create your views here.
