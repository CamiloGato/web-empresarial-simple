from random import randint
from .models import Social

def ctx_social(request):
    context = {'social':Social.objects.all()}
    return context

def ctx_randint(request):
    values = {}
    colors = ['#1B2631','#BA4A00','#145A32','#4A235A','#641E16','#154360','#21618C','#117864']
    int = randint(1,len(colors))
    index = 0
    for v in colors:
        index+=1
        values[index] = v
    context = {'randint':int, 'values':values}
    return context