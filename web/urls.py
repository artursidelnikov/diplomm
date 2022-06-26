from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    #ТОВАРЫ ПОДРОБНЕЕ
    re_path(r'^tovarbittech/(?P<id>.*)/$', views.product, name='products'),
    re_path(r'^tovarstroytech/(?P<id>.*)/$', views.product1, name='products1'),
    re_path(r'^tovarakustik/(?P<id>.*)/$', views.product2, name='products2'),
    re_path(r'^tovarelect/(?P<id>.*)/$', views.product3, name='products3'),
    re_path(r'^tovaryuvelir/(?P<id>.*)/$', views.product4, name='products4'),
    re_path(r'^tovarprochee/(?P<id>.*)/$', views.product5, name='products5'),
    #ТОВАРЫ ДОБАВИТЬ В КОРЗИНУ
    re_path(r'^korz/(?P<id>.*)/$', views.product6, name='products6'),
    re_path(r'^kr/(?P<id>.*)/$', views.product7, name='products7'),
    re_path(r'^kr2/(?P<id>.*)/$', views.product8, name='products8'),
    re_path(r'^kr3/(?P<id>.*)/$', views.product9, name='products9'),
    re_path(r'^kr4/(?P<id>.*)/$', views.product10, name='products10'),
    re_path(r'^kr5/(?P<id>.*)/$', views.product11, name='products11'),
    #КОРЗИНА
    path('/kr', views.korz, name='kz'),
    #ТОВАРЫ УДАЛЕНИЕ ИЗ КОРЗИНЫ
    re_path(r'^ud/(?P<id>.*)/$', views.product12, name='products12'),
    re_path(r'^ud1/(?P<id>.*)/$', views.product13, name='products13'),
    re_path(r'^ud3/(?P<id>.*)/$', views.product14, name='products14'),
    re_path(r'^ud4/(?P<id>.*)/$', views.product15, name='products15'),
    re_path(r'^ud5/(?P<id>.*)/$', views.product16, name='products16'),
    re_path(r'^ud6/(?P<id>.*)/$', views.product17, name='products17'),
    re_path('ot/', views.product18, name='products18'),
]
