from django.contrib import admin
from app.models import Item, Staff, Vendor, QuotationItem, PurchaseOrderProduct, Quotation, PurchaseOrder

admin.site.register(Staff)
admin.site.register(Vendor)
admin.site.register(QuotationItem)
admin.site.register(PurchaseOrderProduct)
admin.site.register(Quotation)
admin.site.register(PurchaseOrder)