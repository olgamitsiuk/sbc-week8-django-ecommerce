from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateField()

    def __str__(self):
        return f"{self.customer_name} {self.product_name} {self.order_date}"
