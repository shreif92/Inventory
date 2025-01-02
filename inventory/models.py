from django.db import models
import uuid
# Create your models here.


class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2,default=1)
    is_deleted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self) -> str:
        return self.name
