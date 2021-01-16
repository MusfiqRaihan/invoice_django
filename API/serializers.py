from rest_framework import serializers
from customer.models import CustomerCompanyInfo, InvoiceInfo, ProductInfo


class CustomerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCompanyInfo
        fields = ['id', 'logo', 'name', 'address', 'created_on']


class InvoiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceInfo
        fields = ['id', 'company_id', 'invoice_number', 'total', 'tax', 'paid', 'grand_total', 'issue_date', 'due_date']


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['id', 'invoice_id', 'item_name', 'quantity', 'unit_price', 'sub_total', 'created_on']
