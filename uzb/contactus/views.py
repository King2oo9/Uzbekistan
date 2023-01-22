from django.shortcuts import render, redirect
from .forms import Cnt
from .models import Contact


# Create your views here.
def asosiy(request):
    if request.method == 'POST':
        ism = request.POST.get('ism')
        mavzu = request.POST.get('mavzu')
        matn = request.POST.get('matn')
        contatc=Contact(ism=ism, mavzu=mavzu, matn=matn)
        contatc.save()
        # form = Cnt(request.POST)
        # if form.is_valid():
        #     form.save()
        #     print('Saqlandi')
        #     return redirect('contact')
        # else:
        #     print('xatolik bor')
    return render(request, 'contactus/index.html')
