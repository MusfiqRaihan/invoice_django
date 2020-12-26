from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from customer import views

urlpatterns = [
    path('', views.get_login, name='login'),
    path('logout/', views.get_logout, name='logout'),
    path('invoice/create', views.get_invoice, name='invoice'),
    path('company/create', views.get_customer_company, name='customer-company'),
    path('items/create', views.get_items, name='customer-items'),
    path('items/delete/<int:id>', views.delete_item, name='delete-items'),
    path('invoice/all', views.all_invoice, name='all_invoice'),
    path('invoice/delete/<int:id>', views.delete_invoice, name='delete-invoice'),
    path('invoice/view/<int:id>', views.view_invoice, name='view-invoice'),
    path('invoice/edit/<int:id>', views.edit_invoice, name='edit-invoice'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
