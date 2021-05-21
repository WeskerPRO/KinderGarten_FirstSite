from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.StaffModel)
class AdminStaffModel(admin.ModelAdmin):
    list_display = ["main_title", "title", "created_at"]
    list_filter = ["main_title"]
    search_fields = ["main_title", "title", "created_at"]


@admin.register(models.AboutChildrenModel)
class AdminAboutChildrenModel(admin.ModelAdmin):
    list_display = ["name_of_first_table", "num_of_first_table", "name_of_second_table", "num_of_second_table",
                    "name_of_third_table", "num_of_third_table", "updated_at"]

    def has_delete_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request):
        if models.AboutChildrenModel.objects.count() > 0:
            pass

        else:
            return super().has_add_permission(request)


@admin.register(models.NewsModel)
class AdminNewsModel(admin.ModelAdmin):
    list_display = ["title", "message", "created_at"]
    list_filter = ["title"]
    search_fields = ["title", "created_at"]


@admin.register(models.GalaryModel)
class AdminGalaryModel(admin.ModelAdmin):
    list_display = ["main_title", "created_at"]
    list_filter = ["main_title"]
    search_fields = ["main_title", "title", "created_at"]


@admin.register(models.ContactModel)
class AdminContactModel(admin.ModelAdmin):
    list_display = ["email", "contact_num", "updated_at"]

    def has_delete_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request):
        if models.ContactModel.objects.count() > 0:
            pass

        else:
            return super().has_add_permission(request)


@admin.register(models.Customer)
class AdminCustomerModel(admin.ModelAdmin):
    list_display = ["name", "phone_number", "message", "created_at"]
    list_filter = ["name", "phone_number"]
    search_fields = ["name", "phone_number", "message", "created_at"]

    def has_add_permission(self, request):
        pass

    def has_change_permission(self, request, obj=None):
        pass


@admin.register(models.BannerModel)
class AdminBannerModel(admin.ModelAdmin):
    list_display = ["banner_main_title", "updated_at"]

    def has_delete_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request):
        if models.BannerModel.objects.count() > 0:
            pass

        else:
            return super().has_add_permission(request)
