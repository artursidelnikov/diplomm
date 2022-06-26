from django.db import models

class Akustiky(models.Model): #для Аудио техники
    id_AkustikY = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    id_kategoriya_aud_tehnika = models.ForeignKey('Kategorii_akustika', null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    Nazvanie = models.CharField(max_length=50, verbose_name="Название")
    Proizvoditel = models.CharField(max_length=20, verbose_name="Производитель")
    potrebl_moshnost = models.IntegerField(verbose_name="Потребляемая мощность")
    vihodnaya_moshnost = models.IntegerField(verbose_name="Выходная мощность")
    blupup = models.CharField(max_length=20, verbose_name="Bluetooth")
    wifi = models.CharField(max_length=20, verbose_name="Wifi")
    Ves = models.IntegerField(verbose_name="Вес")
    gabarit = models.CharField(max_length=14, verbose_name="Габариты")
    dinamiky = models.IntegerField(verbose_name="Динамики")
    diaazon_chastot = models.CharField(max_length=14, verbose_name="Диапазон частот")
    iterfeysy = models.CharField(max_length=60, verbose_name="Интерфейсы")
    oisanye = models.CharField(max_length=1000, verbose_name="Описание")
    foto = models.ImageField(default = 'no_image.jpg', upload_to='product_image')
    Cena = models.IntegerField(default = 0, verbose_name="Цена")
    id_Sostoyanie_veshi = models.ForeignKey('Sostoyanie_veshi', null=True, on_delete=models.SET_NULL, verbose_name="Состояние")

class Kategorii_akustika(models.Model):
    id_kategoriya_aud_tehnika = models.AutoField(primary_key=True, unique=True)
    kategoriya_aud_tehnika = models.CharField(max_length=20)
    def __str__(self):
        return self.kategoriya_aud_tehnika

class Bytovaya_elektronika(models.Model):
    id_Bytovaya_elektronika = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    id_kategoriya_bytovaya_elektronika = models.ForeignKey('kategoriya_bytovaya_elektronika', null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    Nazvanie = models.CharField(max_length=50, verbose_name="Название")
    Proizvoditel = models.CharField(max_length=20, verbose_name="Производитель")
    moshnost = models.IntegerField( verbose_name="Мощность")
    wifi = models.CharField(max_length=20, verbose_name="Wifi")
    gabarit = models.CharField(max_length=14, verbose_name="Габариты")
    dinamiky = models.IntegerField( verbose_name="Динамики")
    Cena = models.IntegerField( verbose_name="Цена")
    oisanye = models.CharField(max_length=1000, verbose_name="Описание")
    foto = models.ImageField(default = 'no_image.jpg', upload_to='product_image')
    id_Sostoyanie_veshi = models.ForeignKey('Sostoyanie_veshi', null=True, on_delete=models.SET_NULL, verbose_name="Состояние")
    def __int__(self):
        return self.id_Bytovaya_elektronika

class kategoriya_bytovaya_elektronika(models.Model):

    id_kategoriya_bytovaya_elektronika = models.AutoField(primary_key=True, unique=True)
    kategoriya_bytovaya_elektronika = models.CharField(max_length=20)
    def __str__(self):
        return self.kategoriya_bytovaya_elektronika

class Paroly(models.Model):
    id_parolya = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    login = models.CharField(max_length=15, verbose_name="Логин")
    Parol = models.CharField(max_length=10, verbose_name="Пароль")
    def __int__(self):
        return self.id_parolya

class Klienty(models.Model):
    id_klient = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    id_parolya = models.OneToOneField('Paroly', null=True, on_delete=models.SET_NULL, verbose_name="Пароль")
    familiya = models.CharField(max_length=30, verbose_name="Фамилия")
    imya = models.CharField(max_length=15, verbose_name="Имя")
    otchestvo = models.CharField(max_length=20, verbose_name="ОТчество")
    seriya = models.IntegerField(verbose_name="Серия")
    nomer = models.IntegerField(verbose_name="Номер")
    telefon = models.IntegerField(verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")

class Dolzhnosty(models.Model):
    id_dolzhnosty = models.AutoField(primary_key=True, unique=True)
    nazvanie = models.CharField(max_length=20)

class Sotrudniky(models.Model):
    id_sotrudnika = models.AutoField(primary_key=True, unique=True)
    id_parolya = models.OneToOneField('Paroly', null=True, on_delete=models.SET_NULL)
    familiya = models.CharField(max_length=30)
    imya = models.CharField(max_length=15)
    otchestvo = models.CharField(max_length=20)
    id_dolzhnosty = models.ForeignKey('Dolzhnosty', null=True, on_delete=models.SET_NULL)
    seriya = models.IntegerField()
    nomer = models.IntegerField()
    adress = models.CharField(max_length=60)
    telefon = models.IntegerField()
    nomer_scheta = models.IntegerField()

class Kategoriya_stroy_elektronika(models.Model):
    id_kategoriya_stroy_elektronika = models.AutoField(primary_key=True, unique=True)
    nazvanie = models.CharField(max_length=20)
    def __str__(self):
        return self.nazvanie

class Stroy_elektronika(models.Model):
    id_Stroy_elektronika = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    id_kategoriya_stroy_elektronika = models.ForeignKey('Kategoriya_stroy_elektronika', null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    Nazvanie = models.CharField(max_length=50, verbose_name="Название")
    Proizvoditel = models.CharField(max_length=20, verbose_name="Производитель")
    moshnost = models.IntegerField(verbose_name="Мощность")
    krutyshy_moment = models.IntegerField( verbose_name="Крутящий момент")
    akkumulyator = models.IntegerField( verbose_name="Аккамулятор")
    ves = models.IntegerField( verbose_name="Вес")
    Cena = models.IntegerField( verbose_name="Цена")
    oisanye = models.CharField(max_length=1000, verbose_name="Описание")
    foto = models.ImageField(default = 'no_image.jpg', upload_to='product_image')
    id_Sostoyanie_veshi = models.ForeignKey('Sostoyanie_veshi', null=True, on_delete=models.SET_NULL, verbose_name="Состояние")

class Kategoriya_elektronika(models.Model):
    id_kategoriya_elektronika = models.AutoField(primary_key=True, unique=True)
    nazvanie = models.CharField(max_length=20)
    def __str__(self):
        return self.nazvanie

class Elektronika(models.Model):
    id_Elektronika = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    id_kategoriya_elektronika = models.ForeignKey('Kategoriya_elektronika', null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    Nazvanie = models.CharField(max_length=50, verbose_name="Название")
    Proizvoditel = models.CharField(max_length=20, verbose_name="Производительность")
    razmer_displeya = models.CharField(max_length=20, verbose_name="Размер дисплея")
    tip_displeya = models.CharField(max_length=20, verbose_name="Тип дисплея")
    cpu = models.CharField(max_length=20, verbose_name="CPU")
    gpu = models.CharField(max_length=20, verbose_name="GPU")
    chastota_CPU = models.CharField(max_length=20, verbose_name="Частота CPU")
    tip_pamyati = models.CharField(max_length=20, verbose_name="Тип памяти")
    objem_pamyaty = models.CharField(max_length=20, verbose_name="Объем памяти")
    interfeysy = models.CharField(max_length=20, verbose_name="Интерфейсы")
    Kamera = models.IntegerField( verbose_name="Камера")
    Cena = models.IntegerField( verbose_name="Цена")
    oisanye = models.CharField(max_length=1000, verbose_name="Описание")
    foto = models.ImageField(default = 'no_image.jpg', upload_to='product_image')
    id_Sostoyanie_veshi = models.ForeignKey('Sostoyanie_veshi', null=True, on_delete=models.SET_NULL, verbose_name="Состояние")

class Kategoriya_yuvelirka(models.Model):
    id_kategoriya_yuvelirka = models.AutoField(primary_key=True, unique=True)
    nazvanie = models.CharField(max_length=20)
    def __str__(self):
        return self.nazvanie

class Yuvelirka(models.Model):
    id_Yuvelirka = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    id_kategoriya_yuvelirka = models.ForeignKey('Kategoriya_yuvelirka', null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    proba = models.IntegerField( verbose_name="Проба")
    ves = models.IntegerField( verbose_name="Вес")
    razmer = models.CharField(max_length=20, verbose_name="Размер")
    vstavka = models.CharField(max_length=20, verbose_name="Вставка")
    Cena = models.IntegerField( verbose_name="Цена")
    oisanye = models.CharField(max_length=1000, verbose_name="Описание")
    foto = models.ImageField(default = 'no_image.jpg', upload_to='product_image')
    id_Sostoyanie_veshi = models.ForeignKey('Sostoyanie_veshi', null=True, on_delete=models.SET_NULL, verbose_name="Состояние")

class Prochee(models.Model):
    id_Prochee = models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    Nazvanie = models.CharField(max_length=50, verbose_name="Название")
    Proizvoditel = models.CharField(max_length=20, verbose_name="Производитель")
    harakteristyki = models.CharField(max_length=1000, verbose_name="Характеристики")
    Cena = models.IntegerField( verbose_name="Цена")
    oisanye = models.CharField(max_length=1000, verbose_name="Описание")
    foto = models.ImageField(default = 'no_image.jpg', upload_to='product_image')
    id_Sostoyanie_veshi = models.ForeignKey('Sostoyanie_veshi', null=True, on_delete=models.SET_NULL, verbose_name="Состояние")

class Sostoyanie_zaloga(models.Model):
    id_sostoyanie_zaloga = models.AutoField(primary_key=True, unique=True)
    nazvanie = models.CharField(max_length=20)

class Zalogovye_bilety(models.Model):
    id_zaloga= models.AutoField(primary_key=True, unique=True)
    id_klient = models.OneToOneField('Klienty', null=True, on_delete=models.SET_NULL)
    id_Akustiky = models.OneToOneField('Akustiky', null=True, on_delete=models.SET_NULL)
    id_Bytovaya_elektronika = models.OneToOneField('Bytovaya_elektronika', null=True, on_delete=models.SET_NULL)
    id_Stroy_elektronika = models.OneToOneField('Stroy_elektronika', null=True, on_delete=models.SET_NULL)
    id_Elektronika = models.OneToOneField('Elektronika', null=True, on_delete=models.SET_NULL)
    id_Yuvelirka = models.OneToOneField('Yuvelirka', null=True, on_delete=models.SET_NULL)
    id_Prochee = models.OneToOneField('Prochee', null=True, on_delete=models.SET_NULL)
    id_sotrudnika = models.OneToOneField('Sotrudniky', null=True, on_delete=models.SET_NULL)
    Summa_zajma = models.IntegerField()
    Summa_procentov = models.IntegerField()
    data_nachala = models.DateField()
    data_okonchaniya = models.DateField()
    id_sostoyanie_zaloga = models.ForeignKey('Sostoyanie_zaloga', null=True, on_delete=models.SET_NULL)

class Rashodnjy_kassovjy_orden(models.Model):
    id_rashodnjy_kassovjy_orden= models.AutoField(primary_key=True, unique=True)
    id_klient = models.OneToOneField('Klienty', null=True, on_delete=models.SET_NULL)
    id_sotrudnika = models.OneToOneField('Sotrudniky', null=True, on_delete=models.SET_NULL)
    id_zaloga = models.OneToOneField('Zalogovye_bilety', null=True, on_delete=models.SET_NULL)

class Tovarnje_cheky(models.Model):
    id_tovarnje_cheky= models.AutoField(primary_key=True, unique=True, verbose_name="ID")
    id_klient = models.OneToOneField('Klienty', null=True, on_delete=models.SET_NULL, verbose_name="Клиент")
    Summa_pokupky = models.IntegerField(verbose_name="Сумма покупки")

class Korzina(models.Model):
    id_Korzina = models.AutoField(primary_key=True, unique=True)
    id_parolya = models.OneToOneField('Paroly', null=True, on_delete=models.SET_NULL)
    id_AkustikY = models.ManyToManyField('Akustiky', null=True)
    id_Bytovaya_elektronika = models.ManyToManyField('Bytovaya_elektronika', null=True)
    id_Stroy_elektronika = models.ManyToManyField('Stroy_elektronika', related_name='targets', blank=True, null=True)
    id_Elektronika = models.ManyToManyField('Elektronika', null=True)
    id_Yuvelirka = models.ManyToManyField('Yuvelirka', null=True)
    id_Prochee = models.ManyToManyField('Prochee',  null=True)

class Sostoyanie_veshi(models.Model):
    id_Sostoyanie_veshi = models.AutoField(primary_key=True, unique=True)
    Sostoyanie = models.CharField(max_length=20)
    def __str__(self):
        return self.Sostoyanie


