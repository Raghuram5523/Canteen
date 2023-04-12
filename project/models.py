from django.db import connections
from django.db import models

# Create your models here.

class OrderConfirmation(models.Model):
    name = models.CharField(max_length=64)
    orders = models.JSONField()
    email = models.CharField(max_length=64)
    payment = models.IntegerField()
    payment_method = models.CharField(max_length=64)
    payment_id = models.CharField(max_length=64)
    date_of_order = models.DateTimeField()
    class Orders:
        db_table = 'project_orderhistory'