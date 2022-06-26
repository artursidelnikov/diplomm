from urllib import request

from django.shortcuts import render, redirect
from web.models import Akustiky
from web.models import Bytovaya_elektronika
from web.models import Stroy_elektronika
from web.models import Elektronika
from web.models import Yuvelirka
from web.models import Prochee
from web.models import Paroly
from web.models import Korzina
from web.models import Sostoyanie_veshi

def product(request, id):
    product = Bytovaya_elektronika.objects.get(id_Bytovaya_elektronika=id)
    lo1 = request.session.get('id_pl', '0')
    product6 = Paroly.objects.all()
    context = {
        'product': product,
        'parol': product6,
        'loo': lo1
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"]=123
        request.session.cycle_key()
        print(request.session.session_key)
    return render (request,'web/product.html', context)

def product1(request, id):
    product = Stroy_elektronika.objects.get(id_Stroy_elektronika=id)
    lo1 = request.session.get('id_pl', '0')
    product6 = Paroly.objects.all()
    context = {
        'product': product,
        'parol': product6,
        'loo': lo1
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"]=123
        request.session.cycle_key()
        print(request.session.session_key)
    return render (request,'web/product1.html', context)

def product2(request, id):
    product = Akustiky.objects.get(id_AkustikY=id)
    lo1 = request.session.get('id_pl', '0')
    product6 = Paroly.objects.all()
    context = {
        'product': product,
        'parol': product6,
        'loo': lo1
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"]=123
        request.session.cycle_key()
        print(request.session.session_key)
    return render (request,'web/product2.html', context)

def product3(request, id):
    product = Elektronika.objects.get(id_Elektronika=id)
    lo1 = request.session.get('id_pl', '0')
    product6 = Paroly.objects.all()
    context = {
        'product': product,
        'parol': product6,
        'loo': lo1
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"]=123
        request.session.cycle_key()
        print(request.session.session_key)
    return render (request,'web/product3.html', context)

def product4(request, id):
    product = Yuvelirka.objects.get(id_Yuvelirka=id)
    lo1 = request.session.get('id_pl', '0')
    product6 = Paroly.objects.all()
    context = {
        'product': product,
        'parol': product6,
        'loo': lo1
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"]=123
        request.session.cycle_key()
        print(request.session.session_key)
    return render (request,'web/product4.html', context)

def product5(request, id):
    product = Prochee.objects.get(id_Prochee=id)
    lo1 = request.session.get('id_pl', '0')
    product6 = Paroly.objects.all()
    context = {
        'product': product,
        'parol': product6,
        'loo': lo1
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"]=123
        request.session.cycle_key()
        print(request.session.session_key)
    return render (request,'web/product5.html', context)

def ppp(request):
    print('a')
    id_pl = request.session['id_pl']
    lo1 = request.session.get('id_pl', '0')
    print(lo1)

def product6(request, id):
    product10 = Bytovaya_elektronika.objects.all()
    lo1 = request.session.get('id_pl', '0')
    tom1 = Korzina.objects.all()
    id_korz = 0
    for p in tom1:  # ищем существует ли корзина у данного пользователя
        ku = Paroly.objects.get(id_parolya=lo1)
        if p.id_parolya == ku:
            id_korz = p.id_Korzina
            break
    if id_korz == 0:
        tom2 = Korzina()
        ku = Paroly.objects.get(id_parolya=lo1)
        K = Korzina(id_parolya=ku)
        K.save()
        id_korz = K.id_Korzina
    tom1 = Korzina.objects.all()
    tom3 = Korzina.objects.get(id_Korzina=id_korz)
    for k in tom1:
        if k == tom3:
            k.id_Bytovaya_elektronika.add(id)
            break
    tom5 = Korzina.objects.get(id_Korzina=id_korz)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product7(request, id):
    product10 = Stroy_elektronika.objects.all()
    lo1 = request.session.get('id_pl', '0')
    tom1 = Korzina.objects.all()
    id_korz = 0
    for p in tom1:#ищем существует ли корзина у данного пользователя
        ku = Paroly.objects.get(id_parolya=lo1)
        if p.id_parolya == ku:
            id_korz = p.id_Korzina
            break
    if id_korz == 0:
        tom2 = Korzina()
        ku = Paroly.objects.get(id_parolya=lo1)
        K = Korzina(id_parolya=ku)
        K.save()
        id_korz = K.id_Korzina
    tom1 = Korzina.objects.all()
    tom3 = Korzina.objects.get(id_Korzina=id_korz)
    for k in tom1:
        if k == tom3:
            k.id_Stroy_elektronika.add(id)
            break
    tom5 = Korzina.objects.get(id_Korzina=id_korz)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product8(request, id):
    product10 = Akustiky.objects.all()
    lo1 = request.session.get('id_pl', '0')
    tom1 = Korzina.objects.all()
    id_korz = 0
    for p in tom1:  # ищем существует ли корзина у данного пользователя
        ku = Paroly.objects.get(id_parolya=lo1)
        if p.id_parolya == ku:
            id_korz = p.id_Korzina
            break
    if id_korz == 0:
        tom2 = Korzina()
        ku = Paroly.objects.get(id_parolya=lo1)
        K = Korzina(id_parolya=ku)
        K.save()
        id_korz = K.id_Korzina
    tom1 = Korzina.objects.all()
    tom3 = Korzina.objects.get(id_Korzina=id_korz)
    for k in tom1:
        if k == tom3:
            k.id_AkustikY.add(id)
            break
    tom5 = Korzina.objects.get(id_Korzina=id_korz)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product9(request, id):
    product10 = Elektronika.objects.all()
    lo1 = request.session.get('id_pl', '0')
    tom1 = Korzina.objects.all()
    id_korz = 0
    for p in tom1:#ищем существует ли корзина у данного пользователя
        ku = Paroly.objects.get(id_parolya=lo1)
        if p.id_parolya == ku:
            id_korz = p.id_Korzina
            break
    if id_korz == 0:
        tom2 = Korzina()
        ku = Paroly.objects.get(id_parolya=lo1)
        K = Korzina(id_parolya=ku)
        K.save()
        id_korz = K.id_Korzina
    tom1 = Korzina.objects.all()
    tom3 = Korzina.objects.get(id_Korzina=id_korz)
    for k in tom1:
        if k == tom3:
            k.id_Elektronika.add(id)
            break
    tom5 = Korzina.objects.get(id_Korzina=id_korz)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product10(request, id):
    product10 = Yuvelirka.objects.all()
    lo1 = request.session.get('id_pl', '0')
    tom1 = Korzina.objects.all()
    id_korz = 0
    for p in tom1:#ищем существует ли корзина у данного пользователя
        ku = Paroly.objects.get(id_parolya=lo1)
        if p.id_parolya == ku:
            id_korz = p.id_Korzina
            break
    if id_korz == 0:
        tom2 = Korzina()
        ku = Paroly.objects.get(id_parolya=lo1)
        K = Korzina(id_parolya=ku)
        K.save()
        id_korz = K.id_Korzina
    tom1 = Korzina.objects.all()
    tom3 = Korzina.objects.get(id_Korzina=id_korz)
    for k in tom1:
        if k == tom3:
            k.id_Yuvelirka.add(id)
            break
    tom5 = Korzina.objects.get(id_Korzina=id_korz)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product11(request, id):
    product10 = Prochee.objects.all()
    lo1 = request.session.get('id_pl', '0')
    tom1 = Korzina.objects.all()
    id_korz = 0
    for p in tom1:#ищем существует ли корзина у данного пользователя
        ku = Paroly.objects.get(id_parolya=lo1)
        if p.id_parolya == ku:
            id_korz = p.id_Korzina
            break
    if id_korz == 0:
        tom2 = Korzina()
        ku = Paroly.objects.get(id_parolya=lo1)
        K = Korzina(id_parolya=ku)
        K.save()
        id_korz = K.id_Korzina
    tom1 = Korzina.objects.all()
    tom3 = Korzina.objects.get(id_Korzina=id_korz)
    for k in tom1:
        if k == tom3:
            k.id_Prochee.add(id)
            break
    tom5 = Korzina.objects.get(id_Korzina=id_korz)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product12(request, id):
    #Строй
    lo1 = request.session.get('id_pl', '0')
    product99=0
    tom1 = Korzina.objects.all()
    ku = Paroly.objects.get(id_parolya=lo1)
    for p in tom1:
        print(p.id_parolya)
        print(ku)
        if p.id_parolya == ku:
            product99 = p.id_Stroy_elektronika
            break
    print(product99.all())
    for y in tom1:
        for u in product99.all():
            if int(u.id_Stroy_elektronika) == int(id):
                y.id_Stroy_elektronika.remove(id)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product13(request, id):
    #Акустик
    lo1 = request.session.get('id_pl', '0')
    product99=0
    tom1 = Korzina.objects.all()
    ku = Paroly.objects.get(id_parolya=lo1)
    for p in tom1:
        print(p.id_parolya)
        print(ku)
        if p.id_parolya == ku:
            product99 = p.id_AkustikY
            break
    print(product99.all())
    for y in tom1:
        for u in product99.all():
            if int(u.id_AkustikY) == int(id):
                y.id_AkustikY.remove(id)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product14(request, id):
    #БытТех
    lo1 = request.session.get('id_pl', '0')
    product99=0
    tom1 = Korzina.objects.all()
    ku = Paroly.objects.get(id_parolya=lo1)
    for p in tom1:
        print(p.id_parolya)
        print(ku)
        if p.id_parolya == ku:
            product99 = p.id_Bytovaya_elektronika
            break
    print(product99.all())
    for y in tom1:
        for u in product99.all():
            if int(u.id_Bytovaya_elektronika) == int(id):
                y.id_Bytovaya_elektronika.remove(id)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product15(request, id):
    #Электр
    lo1 = request.session.get('id_pl', '0')
    product99=0
    tom1 = Korzina.objects.all()
    ku = Paroly.objects.get(id_parolya=lo1)
    for p in tom1:
        print(p.id_parolya)
        print(ku)
        if p.id_parolya == ku:
            product99 = p.id_Elektronika
            break
    print(product99.all())
    for y in tom1:
        for u in product99.all():
            if int(u.id_Elektronika) == int(id):
                y.id_Elektronika.remove(id)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product16(request, id):
    #Ювелирка
    lo1 = request.session.get('id_pl', '0')
    product99=0
    tom1 = Korzina.objects.all()
    ku = Paroly.objects.get(id_parolya=lo1)
    for p in tom1:
        print(p.id_parolya)
        print(ku)
        if p.id_parolya == ku:
            product99 = p.id_Yuvelirka
            break
    print(product99.all())
    for y in tom1:
        for u in product99.all():
            if int(u.id_Yuvelirka) == int(id):
                y.id_Yuvelirka.remove(id)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product17(request, id):
    #Прочее
    lo1 = request.session.get('id_pl', '0')
    product99=0
    tom1 = Korzina.objects.all()
    ku = Paroly.objects.get(id_parolya=lo1)
    for p in tom1:
        print(p.id_parolya)
        print(ku)
        if p.id_parolya == ku:
            product99 = p.id_Prochee
            break
    print(product99.all())
    for y in tom1:
        for u in product99.all():
            if int(u.id_Prochee) == int(id):
                y.id_Prochee.remove(id)
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    lo1 = request.session.get('id_pl', '0')
    context = {
        'akustik': product,
        'bitTech': product1,
        'stroyElect': product2,
        'Elect': product3,
        'Yuvelir': product4,
        'Proche': product5,
        'parol': product6,
        'loo': lo1
    }
    return render(request, 'web/index.html', context)

def product18(request):
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Korzina.objects.all()
    lo1 = request.session.get('id_pl', '0')

    ku1 = Paroly.objects.get(id_parolya=lo1)
    product12 = 0
    product7 = 0
    product8 = 0
    product9 = 0
    product10 = 0
    product11 = 0
    for p in product6:
        if p.id_parolya == ku1:
            product12 = p.id_AkustikY
            product7 = p.id_Bytovaya_elektronika
            product8 = p.id_Stroy_elektronika
            product9 = p.id_Elektronika
            product10 = p.id_Yuvelirka
            product11 = p.id_Prochee
            break
    ku = Sostoyanie_veshi.objects.get(id_Sostoyanie_veshi=4)
    #--------------------быт-тех
    for i1 in product7.all():
        for i in product1:
            if i == i1:
                i.id_Sostoyanie_veshi = ku
                i.save()
        for i3 in product6:
            if i3.id_parolya != ku1:
                for i4 in product7.all():
                    if i1 == i4:
                        i3.id_Bytovaya_elektronika.remove(i1)
    # --------------------строй-тех
    for i1 in product8.all():
        for i in product2:
            if i == i1:
                i.id_Sostoyanie_veshi = ku
                i.save()
        for i3 in product6:
            if i3.id_parolya != ku1:
                for i4 in product8.all():
                    if i1 == i4:
                        i3.id_Stroy_elektronika.remove(i1)
    # --------------------электр------
    for i1 in product9.all():
        for i in product3:
            if i == i1:
                i.id_Sostoyanie_veshi = ku
                i.save()
        for i3 in product6:
            if i3.id_parolya != ku1:
                for i4 in product9.all():
                    if i1 == i4:
                        i3.id_Elektronika.remove(i1)
    # --------------------ювелирка------
    for i1 in product10.all():
        for i in product4:
            if i == i1:
                i.id_Sostoyanie_veshi = ku
                i.save()
        for i3 in product6:
            if i3.id_parolya != ku1:
                for i4 in product10.all():
                    if i1 == i4:
                        i3.id_Yuvelirka.remove(i1)
    # --------------------прочее------
    for i1 in product11.all():
        for i in product5:
            if i == i1:
                i.id_Sostoyanie_veshi = ku
                i.save()
        for i3 in product6:
            if i3.id_parolya != ku1:
                for i4 in product11.all():
                    if i1 == i4:
                        i3.id_Prochee.remove(i1)
    # --------------------акустика------
    for i1 in product12.all():
        for i in product:
            if i == i1:
                i.id_Sostoyanie_veshi = ku
                i.save()
        for i3 in product6:
            if i3.id_parolya != ku1:
                for i4 in product12.all():
                    if i1 == i4:
                        i3.id_AkustikY.remove(i1)
    return redirect('/')

def korz(request):
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Korzina.objects.all()
    product7 = 0
    product8 = 0
    product9 = 0
    product10 = 0
    product11 = 0
    product12 = 0
    lo1 = request.session.get('id_pl', '0')
    ku = Paroly.objects.get(id_parolya=lo1)
    for p in product6:
        print(p.id_parolya)
        print(ku)
        if p.id_parolya == ku:
            product12 = p.id_AkustikY
            product7 = p.id_Bytovaya_elektronika
            product8 = p.id_Stroy_elektronika
            product9 = p.id_Elektronika
            product10 = p.id_Yuvelirka
            product11 = p.id_Prochee
            break
    sum = 0
    # подсчет суммы
    for u in product12.all():
        for u1 in product:
            if u == u1:
                sum = sum + u1.Cena
    for u in product7.all():
        for u1 in product1:
            if u == u1:
                sum = sum + u1.Cena
    for u in product8.all():
        for u1 in product2:
            if u == u1:
                sum = sum + u1.Cena
    for u in product9.all():
        for u1 in product3:
            if u == u1:
                sum = sum + u1.Cena
    for u in product10.all():
        for u1 in product4:
            if u == u1:
                sum = sum + u1.Cena
    for u in product11.all():
        for u1 in product5:
            if u == u1:
                sum = sum + u1.Cena
    context = {
        'akustik' : product,
        'bitTech' : product1,
        'stroyElect' : product2,
        'Elect' : product3,
        'Yuvelir' : product4,
        'Proche' : product5,
        'korz' : product6,
        'korzbitTech': product7,
        'korzstroyElect': product8,
        'korzElect': product9,
        'korzYuvelir': product10,
        'korzProche': product11,
        'korzakustik': product12,
        'loo' : lo1,
        'sum': sum
    }
    return render(request, 'web/korz.html', context)

def index(request):
    product = Akustiky.objects.all()
    product1 = Bytovaya_elektronika.objects.all()
    product2 = Stroy_elektronika.objects.all()
    product3 = Elektronika.objects.all()
    product4 = Yuvelirka.objects.all()
    product5 = Prochee.objects.all()
    product6 = Paroly.objects.all()
    product7 = Sostoyanie_veshi.objects.all()
    lo1 = request.session.get('id_pl', '0')
    A1 = 0
    for u in product7:
        #print(u.id_Sostoyanie_veshi)
        #print(u.Sostoyanie)
        if u.id_Sostoyanie_veshi == 3:
            A1 = u.Sostoyanie
            print(u.Sostoyanie)

    context = {
        'akustik' : product,
        'bitTech' : product1,
        'stroyElect' : product2,
        'Elect' : product3,
        'Yuvelir' : product4,
        'Proche' : product5,
        'parol' : product6,
        'loo' : lo1,
        'A1':A1
    }
    ppp(request)
    return render(request, 'web/index.html', context)

