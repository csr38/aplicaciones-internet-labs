from django.shortcuts import render
from django.core.paginator import Paginator
import requests

import requests

def index(request):
    meme = []
    for x in range(1, 10):
        x+=1
        nene = "https://api.themoviedb.org/3/trending/movie/day?api_key=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMGQ4MTM5NzZmMGMxNmFiYzIyNTU4MGJmODJjZTk5MiIsInN1YiI6IjYwMDRmYzFjOTA0ZjZkMDAzZWM1NGRmMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.r9MO5CQMbjQBpvHwkzGq78hKBd3Z_5M_HuV3k5dOjuw&page=" + str(x)
        nano = requests.get(nene).json()
        nini = nano['results']
        meme.extend(nini)
    paginator = Paginator(meme, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)