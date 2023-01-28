from django.shortcuts import render
from.models import yangiliklar
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='log')
def asosiy(request):
    news = yangiliklar.objects.all()
    context = {
        'news':news
    }
    return render(request, 'yangiliklar/index.html', context)