from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .forms import KlientyForm
from .forms import ParolyForm
from web.models import Paroly
from web.models import Klienty
from web.models import Sotrudniky
from django.http import HttpResponseRedirect

def vihod(request):
    request.session['id_pl'] = -1
    lo1 = request.session.get('id_pl', '0')
    print(lo1)
    print('вы вышли')
    return redirect('/')

def create(request):
    if request.method == "POST":
        tom1 = Paroly()
        tom1.login = request.POST.get("login")
        tom1.Parol = request.POST.get("parol")
        tom1.save()
        tom2 = Klienty()
        pr = Paroly.objects.all()
        ku = Paroly.objects.get(login=request.POST.get("login"))
        print(ku.id_parolya)
        request.session['id_pl'] = ku.id_parolya
        K = Klienty(id_parolya = ku, familiya = request.POST.get("familia"), imya = request.POST.get("name"), otchestvo = request.POST.get("otchestvo"), seriya = request.POST.get("seria"), nomer = request.POST.get("nomer"), telefon = request.POST.get("telefon"), email = request.POST.get("pocta") )
        K.save()
        return redirect('/')
    return render(request, 'web/registration.html')

def login(request):
    if request.method == "POST":
        ku = Paroly.objects.get(login=request.POST.get("login"), Parol=request.POST.get("parol"))
        print(ku.id_parolya)
        request.session['id_pl'] = ku.id_parolya
        kli = Klienty.objects.all()
        for t in kli:
            if t.id_parolya == ku:
                return redirect('/')
        sotr = Sotrudniky.objects.all()
        for t1 in sotr:
            if t1.id_parolya == ku:
                print(t1.id_dolzhnosty.id_dolzhnosty)
                if 1 == t1.id_dolzhnosty.id_dolzhnosty:
                    return redirect('/admin/')
                if 2 == t1.id_dolzhnosty.id_dolzhnosty:
                    return redirect('/admin/')
    return render(request, 'web/login.html')



