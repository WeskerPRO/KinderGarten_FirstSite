from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.StaffModel)
class AdminStaffModel(admin.ModelAdmin):
    list_display = ["main_title", "created_at", "updated_at"]
    list_filter = ["main_title"]
    search_fields = ["main_title", "title"]


@admin.register(models.AboutChildrenModel)
class AdminAboutChildrenModel(admin.ModelAdmin):
    list_display = ["name_of_first_table", "num_of_first_table", "name_of_second_table", "num_of_second_table",
                    "name_of_third_table", "num_of_third_table", "updated_at"]


@admin.register(models.NewsModel)
class AdminNewsModel(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]
    list_filter = ["title"]
    search_fields = ["title", "created_at"]


@admin.register(models.GalaryModel)
class AdminGalaryModel(admin.ModelAdmin):
    list_display = ["main_title", "created_at", "updated_at"]
    list_filter = ["main_title"]
    search_fields = ["main_title", "title", "created_at"]


@admin.register(models.ContactModel)
class AdminContactModel(admin.ModelAdmin):
    list_display = ["location", "email", "contact_num", "updated_at"]


@admin.register(models.Customer)
class AdminCustomerModel(admin.ModelAdmin):
    list_display = ["name", "phone_number", "message", "created_at"]
    list_filter = ["name", "phone_number"]
    search_fields = ["name", "phone_number", "message"]


@admin.register(models.BannerModel)
class AdminBannerModel(admin.ModelAdmin):
    list_display = ["banner_main_title", "banner_message_on_title", "updated_at"]
