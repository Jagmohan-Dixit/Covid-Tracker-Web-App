from django.shortcuts import render ,HttpResponse
import requests
import matplotlib.pyplot as plt
# Create your views here.
def index(request):
    data = True
    result = None
    globalsummary = None
    countries = None

    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            globalsummary = result.json()['Global']
            countries = result.json()['Countries']


            data = False
        except:
            data = True



    return render(request,'index.html',{'globalsummary' : globalsummary,'countries':countries,})
  
