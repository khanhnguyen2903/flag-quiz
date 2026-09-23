from django.shortcuts import render
from .models import Flag

def game(request):
    flags = Flag.objects.all()
    flag_data = [ 
        { 
            "id": flag.id, 
            "country_name": flag.country_name, 
            "capital_name" : flag.capital_name,
            "continent" : flag.continent,
            "url_flag": flag.url_flag, 
        } 
        for flag in flags 
    ]
    context = {
        "flags": flag_data
    }
    return render(request, 'quiz/game.html', context)
