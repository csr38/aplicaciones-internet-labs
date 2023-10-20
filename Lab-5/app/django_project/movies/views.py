from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    query = request.GET.get('q')
    results = []


    if query:
        url = "https://apis.digital.gob.cl/fl/feriados/"+query

        headers = {
            "accept": "application/json",
            "Accept-Encoding":	"gzip, deflate, br",
            "Accept-Language":	"es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection":"keep-alive",
            "Host": "apis.digital.gob.cl",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-User":"?1",
            "Upgrade-Insecure-Requests":	"1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"
        }
    

        data = requests.get(url, headers=headers)

        print(data.json())

        for feriado in data.json():
            print(feriado["nombre"])
            results.append({"nombre": feriado["nombre"], "fecha":feriado['fecha'], "tipo":feriado['tipo']})
    else:
        return HttpResponse("No query provided")
    
    return render(request, 'index.html', {"results":results})

