from django.shortcuts import render
import requests
from django.http import HttpResponse


def search(request):
    
    query = request.GET.get('q')
    results = []

    if query:
        url = "https://api.themoviedb.org/3/search/movie?query="+query +"&include_adult=false&language=es-ES&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMGQ4MTM5NzZmMGMxNmFiYzIyNTU4MGJmODJjZTk5MiIsInN1YiI6IjYwMDRmYzFjOTA0ZjZkMDAzZWM1NGRmMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.r9MO5CQMbjQBpvHwkzGq78hKBd3Z_5M_HuV3k5dOjuw"
        }
        data = requests.get(url, headers=headers)

        for movie in data.json()['results']:
            results.append({"name": movie["title"], "poster":movie['poster_path'], "descripcion":movie['overview']})
    else:
        return HttpResponse("No query provided")
    
    return render(request, 'results.html',{
        "results": results,
    })


def index(request):
    return render(request, 'index.html')
