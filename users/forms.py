from django import forms
from web.models import Paroly
from web.models import Klienty
from django.forms import ModelForm, TextInput

class ParolyForm(ModelForm):
    class Meta:
        model = Paroly
        fields = ['login', 'Parol']

        widgets = {
            "login" : TextInput(attrs={
                'class' : 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder' : 'Логин'}),
            "Parol": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Пароль'}),
        }

class KlientyForm(ModelForm):
    class Meta:
        model = Klienty
        fields = [ 'familiya',  'imya', 'otchestvo', 'seriya', 'nomer', 'telefon', 'email']
        widgets = {
            "familiya": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Фамилия'}),
            "imya": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Имя'}),
            "otchestvo": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Отчество'}),
            "seriya": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Серия'}),
            "nomer": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Номер'}),
            "telefon": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Телефон'}),
            "email": TextInput(attrs={
                'class': 'Portfolio-nav wow fadeIn delay-02s',
                'placeholder': 'Почта'}),
        }