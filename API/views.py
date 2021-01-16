from customer.models import CustomerCompanyInfo, InvoiceInfo, ProductInfo
from .serializers import CustomerCompanySerializer, InvoiceInfoSerializer, ProductInfoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CustomerCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = CustomerCompanyInfo.objects.all()
    serializer_class = CustomerCompanySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class InvoiceModelViewSet(viewsets.ModelViewSet):
    queryset = InvoiceInfo.objects.all()
    serializer_class = InvoiceInfoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

