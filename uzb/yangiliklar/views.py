from django.shortcuts import render
from.models import yangiliklar

# Create your views here.
def asosiy(request):
    news = yangiliklar.objects.all()
    context = {
        'news':news
    }
    return render(request, 'yangiliklar/index.html', context)