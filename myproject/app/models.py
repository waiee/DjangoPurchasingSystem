"""
Latest by 22/1/2023 930PM

-- Definition of models --
1. Staff
2. Vendor
3. QuotationItem
4. PurchaseOrderProduct
5. Quotation
6. Purchase Order
"""
from django.db import models
from django.contrib.auth.models import User

#class 

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.TextField()
    item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)

class Staff(models.Model):
    staffID = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.staffID)

class Vendor(models.Model):
    vendorID = models.CharField(primary_key=True, max_length=10)
    vendorName = models.TextField(max_length=20, null=True)
    vendorAddress = models.TextField(max_length=100, null=True)
    vendorContact = models.TextField(null=True)

    def __str__(self):
        return str(self.vendorID)

class Quotation(models.Model):
    quotationID = models.CharField(primary_key=True, max_length=10)
    staffID = models.ForeignKey(Staff,default=None, on_delete=models.CASCADE, null=True)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    totalPrice = models.FloatField(default=None, null=True)
    validityDate = models.DateField()
    qtyProvided = models.IntegerField(null=True)
    quotationStatus = models.CharField(max_length=20, default="Pending")
    selected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.quotationID)

class QuotationItem(models.Model):
    itemID = models.CharField(primary_key=True, max_length=10)
    quotationID = models.ForeignKey(Quotation, default=None, on_delete=models.CASCADE,null=True)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE,null=True)
    itemName = models.TextField(max_length=40, null=True)
    itemPriceperUnit = models.FloatField(default=None, null=True)
    itemPurchased = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.itemID)

class PurchaseOrder(models.Model):
    purchaseOrderID = models.CharField(primary_key=True, max_length=10)
    staffID = models.ForeignKey(Staff,default=None, on_delete=models.CASCADE)
    quotationID = models.ForeignKey(Quotation,default=None, on_delete=models.CASCADE)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    qtyNeeded = models.IntegerField(default=None, null=True)
    qtyProvided = models.IntegerField()
    totalPrice = models.FloatField(default=None, null=True)
    poStatus = models.CharField(max_length=20, default="Pending")
    selected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.purchaseOrderID)

class PurchaseOrderProduct(models.Model):
    productID = models.CharField(primary_key=True, max_length=10)
    purchaseOrderID = models.ForeignKey(PurchaseOrder, default=None, on_delete=models.CASCADE,null=True)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    productName = models.TextField(max_length=40, null=True)
    productPriceperUnit = models.FloatField(default=None, null=True)
    productPurchased = models.BooleanField(default=False)

    def __str__(self):
        return str(self.productID)
