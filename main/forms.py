from django.forms import ModelForm
from . import models
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
import re as regex


def checker_of_phone_number(phone_number):
    result = regex.match("^\+(998)[0-9]{9}$", phone_number)
    result = bool(result)  # well we convert our regex expression to boolean then it will return us true or false!

    if result is False:
        raise ValidationError("Kiritilayotgan ma'lumot no'tog'ri!")


class InputForm(ModelForm):  # We could use Form too but for now I am learning ModelForm which is connected to models.py
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Xabaringizni kiriting"}),
                              max_length=1500, required=True)
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ismingizni kiriting", "style": "color: black"}),
        max_length=13, required=True)

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Telefon raqamingizni kiriting (+998555555555)"}),
        max_length=13, required=True, validators=[checker_of_phone_number])

    phone_number.label = "Telefon raqamingiz"
    name.label = "Ismingiz"
    message.label = "Ma'lumotingiz"

    class Meta:
        model = models.Customer
        fields = ["phone_number", "name", "message"]
    # exclude = ["created_at"]
