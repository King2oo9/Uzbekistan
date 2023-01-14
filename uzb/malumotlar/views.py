from django.shortcuts import render
from.models import malumotlar

# Create your views here.
def asosiy(request):
    malumot = malumotlar.objects.all()
    context = {
        'malumot': malumot
    }
    return render(request, 'malumotlar/index.html', context)