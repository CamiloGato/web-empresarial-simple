from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()

    for link in links:
        ctx[link.key] = link.url
    
    return ctx

def ctx_social(request):
    social = {'social': Link.objects.all()}
    return social 