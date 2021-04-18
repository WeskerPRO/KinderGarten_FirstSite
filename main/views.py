from django.shortcuts import render
# from django.http import HttpResponse
from .models import GalaryModel, ContactModel, NewsModel, AboutChildrenModel, StaffModel, BannerModel
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings


def about(request):  # SECTION --> ABOUT
    PointingContacting = ContactModel.objects.first()
    PointingCounting = AboutChildrenModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "Counts": PointingCounting,
        "Staff": StaffModel.objects.all(),
        "News": NewsModel.objects.all(),
        "Galary": GalaryModel.objects.all(),
        "Banner": BannerModel.objects.first()
    }

    return render(request, "index.html", Input)


def staff(request):  # SECTION --> STAFF
    PointingContacting = ContactModel.objects.first()
    PointingCounting = AboutChildrenModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "Staff": StaffModel.objects.all(),
        "Counts": PointingCounting,
        "Banner": BannerModel.objects.first()
    }

    return render(request, "index-staff.html", Input)


def news(request):  # SECTION --> NEWS
    PointingContacting = ContactModel.objects.first()
    PointingNews = NewsModel.objects.all()
    PointingCounting = AboutChildrenModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "News": PointingNews,
        "Counts": PointingCounting,
        "Banner": BannerModel.objects.first()
    }

    return render(request, "index-news.html", Input)


def galary(request):  # SECTION --> GALARY
    PointingContacting = ContactModel.objects.first()
    GalaryAnswer = GalaryModel.objects.all()
    PointingCounting = AboutChildrenModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "Galary": GalaryAnswer,
        "Counts": PointingCounting,
        "Banner": BannerModel.objects.first()
    }

    return render(request, "index-galary.html", Input)


def contact(request):  # SECTION --> CONTACT
    Submit = False
    phone_error = False

    if request.method == 'POST':
        Forum = forms.InputForm(request.POST)

        if Forum.is_valid():
            Forum.save()
            subject = f"Message from {Forum.cleaned_data['name']} and {Forum.cleaned_data['phone_number']}"
            message = f"{Forum.cleaned_data['message']}"
            host = f"{settings.EMAIL_HOST_USER}"
            To = ["yulchiebahodir@gmail.com"]
            send_mail(subject, message, host, To, True)
            # /contact/ --> /contact/?submitted=True
            # send_main(String Subject, String Message, String FromEmail, [String ToEmail], boolean NotShowAnError)
            return HttpResponseRedirect("?submitted=True")  # FIXED BAD RE LOADING AND INSERTING INFO TO DATABASE!
        else:
            error_response = f"?Error={'PhoneInvalid' if bool(Forum['phone_number'].errors) is True else 'Invalid'}"
            return HttpResponseRedirect(error_response)

    elif request.GET.get("submitted") == "True":
        Submit = True

    elif request.GET.get("Error") == "PhoneInvalid":
        phone_error = True

    PointingContacting = ContactModel.objects.first()
    PointingCounting = AboutChildrenModel.objects.first()
    Forum = forms.InputForm()

    Input = {
        "Forum": Forum,
        "AboutContact": PointingContacting,
        "Submitted": Submit,
        "Counts": PointingCounting,
        "Is_Phone_Valid": phone_error,
        "Banner": BannerModel.objects.first()
    }

    return render(request, "index-contact.html", Input)
