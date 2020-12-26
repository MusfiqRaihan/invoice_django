from django.contrib import admin
from .models import CompanyInfo, BankInfo

admin.site.site_header = 'INVOICE ADMIN PANEL'


class CompanyInfoModel(admin.ModelAdmin):
    list_display = ["__str__", "name", "email", "phone"]
    list_per_page = 10

    class Meta:
        model = CompanyInfo


admin.site.register(CompanyInfo, CompanyInfoModel)


class BankInfoModel(admin.ModelAdmin):
    list_display = ["__str__", "bank_name", "account_type", "account_name", "account_number"]
    list_per_page = 10

    class Meta:
        model = BankInfo


admin.site.register(BankInfo, BankInfoModel)
