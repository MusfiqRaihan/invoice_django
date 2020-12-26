from django import forms
from .models import CustomerCompanyInfo, InvoiceInfo, ProductInfo


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = CustomerCompanyInfo
        fields = [
            'logo',
            'name',
            'address',
        ]


class CreateInvoiceForm(forms.ModelForm):
    class Meta:
        model = InvoiceInfo
        fields = [
            'company_id',
            'due_date',
        ]


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = [
            'item_name',
            'quantity',
            'unit_price',
        ]


class CreatePaidForm(forms.ModelForm):
    class Meta:
        model = InvoiceInfo
        fields = [
            'paid',
        ]
