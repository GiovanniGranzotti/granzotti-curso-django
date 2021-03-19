from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Olá Django. Um beijo para Meire, meu amor S2.')
