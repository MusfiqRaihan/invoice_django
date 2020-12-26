from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CompanyInfo(models.Model):

    logo = models.ImageField(upload_to="Company_logo")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = PhoneNumberField(null=False, blank=False, unique=True, max_length=14)
    website = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name


class BankInfo(models.Model):
    bank_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    account_name = models.CharField(max_length=200)
    account_number = models.IntegerField(null=False, blank=False, unique=True)
    branch_name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=50)
    routing_number = models.IntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.bank_name

