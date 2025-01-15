from django.db import models
import uuid
from inventory.models import *

# Create your models here.


class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    phone = models.IntegerField(unique=True)
    adress = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    gstn = models.CharField(max_length=15,unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    

class PrchaseItem(models.Model):
    billno = models.ForeignKey('PurchasBill', on_delete=models.CASCADE, related_name='PurchasBillno')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='Stock')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    def __str__(self) -> str:
        return "Bill no: " + str(self.billno.billno) + " | Item: " + str(self.stock.name)

class PurchasBill(models.Model):
    billno = models.UUIDField(primary_key=True, default=uuid.uuid4)
    time = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name= 'purchasespupplier')

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_total_price(self):
        purchasitems = PrchaseItem.objects.filter(billno=self)
        total = 0
        for item in purchasitems:
            total += item.totalprice
        return total