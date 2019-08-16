from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'first_app/home.html', {})
def date_actuelle(request):
    return render(request, 'first_app/date.html', {'date': datetime.now()})
