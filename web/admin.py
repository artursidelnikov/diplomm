from email.mime import image

from django.contrib import admin

from web.models import Akustiky
from web.models import Kategorii_akustika
from web.models import Bytovaya_elektronika
from web.models import kategoriya_bytovaya_elektronika
from web.models import Paroly
from web.models import Klienty
from web.models import Dolzhnosty
from web.models import Sotrudniky
from web.models import Kategoriya_stroy_elektronika
from web.models import Stroy_elektronika
from web.models import Kategoriya_elektronika
from web.models import Elektronika
from web.models import Kategoriya_yuvelirka
from web.models import Yuvelirka
from web.models import Prochee
from web.models import Sostoyanie_zaloga
from web.models import Zalogovye_bilety
from web.models import Rashodnjy_kassovjy_orden
from web.models import Tovarnje_cheky
from web.models import Korzina
from web.models import Sostoyanie_veshi
from django.utils.safestring import mark_safe

@admin.register(Korzina)
class KorzinaAdmin(admin.ModelAdmin):
    pass

@admin.register(Sostoyanie_veshi)
class Sostoyanie_veshiAdmin(admin.ModelAdmin):
    pass


@admin.register(Akustiky)
class AkustikyAdmin(admin.ModelAdmin):
    list_display = ("id_AkustikY", "id_kategoriya_aud_tehnika", "Nazvanie", "Proizvoditel", "potrebl_moshnost", "vihodnaya_moshnost", "blupup", "wifi", "Ves", "gabarit", "dinamiky", "diaazon_chastot", "iterfeysy", "oisanye", "image_show", "Cena", "id_Sostoyanie_veshi")

    def image_show(self, obj):
        if obj.foto:
            return mark_safe("<img src='{}' width='60' />".format(obj.foto.url))
        return None
    image_show.__name__ = "Картинка"

@admin.register(Kategorii_akustika)
class Kategorii_akustikaAdmin(admin.ModelAdmin):
    list_display = ("id_kategoriya_aud_tehnika", "kategoriya_aud_tehnika")

@admin.register(Bytovaya_elektronika)
class Bytovaya_elektronikaAdmin(admin.ModelAdmin):
    list_display = ("id_Bytovaya_elektronika", "id_kategoriya_bytovaya_elektronika", "Nazvanie", "Proizvoditel", "moshnost", "wifi", "gabarit", "dinamiky", "Cena", "oisanye", "image_show", "id_Sostoyanie_veshi")
    def image_show(self, obj):
        if obj.foto:
            return mark_safe("<img src='{}' width='60' />".format(obj.foto.url))
        return None
    image_show.__name__ = "Картинка"

@admin.register(kategoriya_bytovaya_elektronika)
class kategoriya_bytovaya_elektronikaAdmin(admin.ModelAdmin):
    pass

@admin.register(Paroly)
class ParolyAdmin(admin.ModelAdmin):
    pass

@admin.register(Klienty)
class KlientyAdmin(admin.ModelAdmin):
    list_display = ("id_klient", "id_parolya", "familiya", "imya", "otchestvo", "seriya", "nomer", "telefon", "email")

@admin.register(Dolzhnosty)
class DolzhnostyAdmin(admin.ModelAdmin):
    pass

@admin.register(Sotrudniky)
class SotrudnikyAdmin(admin.ModelAdmin):
    pass

@admin.register(Kategoriya_stroy_elektronika)
class Kategoriya_stroy_elektronikaAdmin(admin.ModelAdmin):
    pass

@admin.register(Stroy_elektronika)
class Stroy_elektronikaAdmin(admin.ModelAdmin):
    list_display = ("id_Stroy_elektronika", "id_kategoriya_stroy_elektronika", "Nazvanie", "Proizvoditel", "moshnost", "krutyshy_moment", "akkumulyator", "ves", "Cena", "oisanye", "image_show", "id_Sostoyanie_veshi")
    def image_show(self, obj):
        if obj.foto:
            return mark_safe("<img src='{}' width='60' />".format(obj.foto.url))
        return None
    image_show.__name__ = "Картинка"
@admin.register(Kategoriya_elektronika)
class Kategoriya_elektronikaAdmin(admin.ModelAdmin):
    pass

@admin.register(Kategoriya_yuvelirka)
class Kategoriya_yuvelirkaAdmin(admin.ModelAdmin):
    pass

@admin.register(Elektronika)
class ElektronikaAdmin(admin.ModelAdmin):
    list_display = ("id_Elektronika", "id_kategoriya_elektronika", "Nazvanie", "Proizvoditel", "razmer_displeya", "tip_displeya", "cpu", "gpu", "chastota_CPU", "tip_pamyati", "objem_pamyaty", "interfeysy", "Kamera", "Cena", "oisanye", "image_show", "id_Sostoyanie_veshi")
    def image_show(self, obj):
        if obj.foto:
            return mark_safe("<img src='{}' width='60' />".format(obj.foto.url))
        return None
    image_show.__name__ = "Картинка"

@admin.register(Yuvelirka)
class YuvelirkaAdmin(admin.ModelAdmin):
    list_display = ("id_Yuvelirka", "id_kategoriya_yuvelirka", "proba", "ves", "razmer", "vstavka", "Cena", "oisanye", "image_show", "id_Sostoyanie_veshi")
    def image_show(self, obj):
        if obj.foto:
            return mark_safe("<img src='{}' width='60' />".format(obj.foto.url))
        return None
    image_show.__name__ = "Картинка"

@admin.register(Prochee)
class ProcheeAdmin(admin.ModelAdmin):
    list_display = ("id_Prochee", "Nazvanie", "Proizvoditel", "harakteristyki", "Cena", "oisanye", "image_show", "id_Sostoyanie_veshi")
    def image_show(self, obj):
        if obj.foto:
            return mark_safe("<img src='{}' width='60' />".format(obj.foto.url))
        return None
    image_show.__name__ = "Картинка"

@admin.register(Sostoyanie_zaloga)
class Sostoyanie_zalogaAdmin(admin.ModelAdmin):
    pass

@admin.register(Zalogovye_bilety)
class Zalogovye_biletyAdmin(admin.ModelAdmin):
    pass

@admin.register(Rashodnjy_kassovjy_orden)
class Rashodnjy_kassovjy_ordenAdmin(admin.ModelAdmin):
    pass

@admin.register(Tovarnje_cheky)
class Tovarnje_chekyAdmin(admin.ModelAdmin):
    list_display = ("id_tovarnje_cheky", "id_klient", "Summa_pokupky")


