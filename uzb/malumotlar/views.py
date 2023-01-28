from django.shortcuts import render
from .models import malumotlar
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='log')
def asosiy(request):
    malumot = malumotlar.objects.all()
    context = {
        'malumot': malumot
    }
    return render(request, 'malumotlar/index.html', context)
