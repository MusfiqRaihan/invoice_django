
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from API import views
from rest_framework.routers import DefaultRouter

from django.views.static import serve
from django.conf.urls import url

router = DefaultRouter()

router.register('companyapi', views.CustomerCompanyModelViewSet, basename='company')
router.register('invoiceapi', views.InvoiceModelViewSet, basename='invoice')
router.register('productapi', views.ProductModelViewSet, basename='product')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("customer.urls")),
    path('router', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
