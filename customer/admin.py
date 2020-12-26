from django.contrib import admin
from customer.models import CustomerCompanyInfo, InvoiceInfo, ProductInfo

admin.site.site_header = 'INVOICE ADMIN PANEL'


class CustomerCompanyInfoModel(admin.ModelAdmin):
    list_display = ["__str__", "address", "created_on"]
    list_per_page = 10

    class Meta:
        model = CustomerCompanyInfo


admin.site.register(CustomerCompanyInfo, CustomerCompanyInfoModel)


class InvoiceInfoModel(admin.ModelAdmin):
    list_display = ["__str__", "company_id", "total", "tax", "paid", "issue_date", "due_date"]
    list_per_page = 10
    list_filter = ["company_id"]

    class Meta:
        model = InvoiceInfo


admin.site.register(InvoiceInfo, InvoiceInfoModel)


class ProductInfoModel(admin.ModelAdmin):
    list_display = ["__str__", "item_name", "unit_price", "quantity", "sub_total"]
    list_per_page = 10
    list_filter = ["invoice_id"]

    class Meta:
        model = ProductInfo


admin.site.register(ProductInfo, ProductInfoModel)



