from django.db import models
import datetime

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomerCompanyInfo(models.Model):
    logo = models.ImageField(upload_to="Customer_company_logo", null=True, blank=True, default='default.jpg')
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class InvoiceInfo(models.Model):
    company_id = models.ForeignKey(CustomerCompanyInfo, on_delete=models.CASCADE)
    invoice_number = models.IntegerField(editable=False, unique=True)
    total = models.FloatField(editable=False, blank=True, null=True)
    tax = models.FloatField(editable=False, blank=True, null=True)
    paid = models.FloatField(editable=True, blank=False, default=0)
    grand_total = models.FloatField(editable=False, blank=True, null=True)
    issue_date = models.DateField(auto_now=False, auto_now_add=True)
    due_date = models.DateField(auto_now=False, auto_now_add=False)

    # def save(self, *args, **kwargs):
    #     now = datetime.datetime.now()
    #     year = now.year
    #     month = now.month
    #     day = now.day
    #     hour = now.strftime("%H")
    #     minute = now.strftime("%M")
    #     second = now.strftime("%S")
    #
    #     gen = str(year) + str(month) + str(day) + str(hour) + str(minute) + str(second)
    #     self.invoice_number = gen
    #     super(InvoiceInfo, self).save(*args, **kwargs)



    def __str__(self):
        return str(self.invoice_number)


class ProductInfo(models.Model):
    invoice_id = models.ForeignKey(InvoiceInfo, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField()
    sub_total = models.FloatField(editable=False, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        self.sub_total = self.unit_price * self.quantity
        super(ProductInfo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.invoice_id)


# this signal creates auth token for users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
