import datetime

from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from company.models import BankInfo, CompanyInfo
from .forms import CreateCompanyForm, CreateInvoiceForm, CreateProductForm, CreatePaidForm
from django.contrib import messages
from customer.models import InvoiceInfo, ProductInfo
from django.http import HttpResponseRedirect


def edit_invoice(request, id):
    if request.user.is_authenticated:
        invoice = InvoiceInfo.objects.get(pk=id)

        print(invoice.paid)

        items = ProductInfo.objects.all().filter(invoice_id=invoice)
        total = 0
        for i in items:
            total = total + i.sub_total

        form2 = CreatePaidForm(request.POST or None)
        if form2.is_valid():
            instance = form2.save(commit=False)
            instance.company_id = invoice.company_id
            instance.invoice_number = invoice.invoice_number
            invoice.paid = instance.paid + invoice.paid
            instance.due_date = invoice.due_date
            net = invoice.total + float(invoice.tax)
            grand_total = float(net) - invoice.paid
            invoice.grand_total = grand_total
            invoice.save()
            print(invoice.paid)
            return redirect('all_invoice')

        context = {
            "items": items,
            "total": total,
            "inv": invoice,
            "form2": form2,
        }

        return render(request, 'edit_invoice.html', context)



    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def get_items(request):
    if request.user.is_authenticated:
        form = CreateProductForm(request.POST or None)
        obj = InvoiceInfo.objects.latest('invoice_number')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.invoice_id = obj
            instance.save()
            messages.success(request, 'Product Added Successfully!')
            return HttpResponseRedirect(request.path_info)

        items = ProductInfo.objects.all().filter(invoice_id=obj)
        inv = get_object_or_404(InvoiceInfo, id=obj.id)

        total = 0
        for i in items:
            total = total + i.sub_total

        amount = 0.075
        tax = total * amount

        inv.tax = tax
        inv.total = total

        net = inv.total + float(inv.tax)
        grand_total = float(net) - inv.paid
        inv.grand_total = grand_total

        inv.save()


        form2 = CreatePaidForm(request.POST or None)
        if form2.is_valid():
            instance = form2.save(commit=False)
            instance.company_id = inv.company_id
            instance.invoice_number = inv.invoice_number
            inv.paid = instance.paid
            instance.issue_date = inv.issue_date
            instance.due_date = inv.due_date
            messages.success(request, 'Paid Amount Saved')
            inv.save()
            # instance.save()
            return redirect('customer-items')

        context = {
            "form": form,
            "items": items,
            "total": total,
            "inv": inv,
            "form2": form2,
        }

        return render(request, 'items.html', context)


    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def view_invoice(request, id):
    if request.user.is_authenticated:
        owner_company = CompanyInfo.objects.all()[0]
        bank_info = BankInfo.objects.all()[0]
        invoice = InvoiceInfo.objects.get(pk=id)
        product = ProductInfo.objects.all().filter(invoice_id=invoice)

        total = 0
        count = 0
        for prod in product:
            total = total + prod.sub_total
            count = count + 1

        amount = 0.075
        tax = total * amount

        invoice.tax = tax
        invoice.total = total

        net = invoice.total + float(invoice.tax)
        grand_total = float(net) - invoice.paid
        invoice.grand_total = grand_total

        invoice.save()

        count = 7 - count

        context = {
            "owner": owner_company,
            "items": product,
            "bank": bank_info,
            "invoice": invoice,
            "counter": range(count),
        }
        return render(request, 'final.html', context)

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def delete_invoice(request, id):
    if request.user.is_authenticated:
        inv = get_object_or_404(InvoiceInfo, id=id)
        inv.delete()
        return redirect('all_invoice')

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def delete_item(request, id):
    if request.user.is_authenticated:
        item = get_object_or_404(ProductInfo, id=id)
        item.delete()
        return redirect('customer-items')

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def get_invoice(request):
    if request.user.is_authenticated:
        form = CreateInvoiceForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            now = datetime.datetime.now()
            year = now.year
            month = now.month
            day = now.day
            hour = now.strftime("%H")
            minute = now.strftime("%M")
            second = now.strftime("%S")

            gen = str(year) + str(month) + str(day) + str(hour) + str(minute) + str(second)
            instance.invoice_number = gen

            instance.save()
            messages.success(request, 'Invoice generated Successfully!')
            return redirect('customer-items')

        context = {
            "form": form,
        }
        return render(request, 'invoice.html', context)


    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def get_customer_company(request):
    if request.user.is_authenticated:
        form = CreateCompanyForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Company Information i'
                                      's Saved! ')
            return redirect('invoice')

        context = {
            "form": form,
        }
        return render(request, 'customer_company.html', context)


    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def get_login(request):
    if request.user.is_authenticated:
        return redirect('all_invoice')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('all_invoice')

            else:
                messages.error(request, 'Username Or Password Mismatch!')

    return render(request, 'login.html')


def get_logout(request):
    logout(request)
    return redirect('login')


def all_invoice(request):
    if request.user.is_authenticated:
        inv = InvoiceInfo.objects.all().order_by('-issue_date')
        search = request.GET.get('index_search')
        if search:
            inv = inv.filter(
                Q(invoice_number__icontains=search)
            )

        return render(request, 'all_invoice.html', {"inv": inv})

# def final_view(request):
#     if request.user.is_authenticated:
#         owner_company = CompanyInfo.objects.all()
#         bank_info = BankInfo.objects.all()
#         obj = InvoiceInfo.objects.latest('invoice_number')
#         items = ProductInfo.objects.all().filter(product_id=obj)
#
#         context = {
#             "owner": owner_company,
#             "bank": bank_info,
#             "items": items,
#         }
#         return render(request, 'final.html', context)
#
#
#     else:
#         return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
#                                     '<a href="/">LOGIN</a></h1>')
#
#
