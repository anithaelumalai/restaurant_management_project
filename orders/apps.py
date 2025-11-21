from django.apps import AppConfig
from django.utils import timezone
class OrderStatus(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def_str_(self):
        return self.name
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    def_str_(self):
        return f"Order #{self.id} -{self.customer_name}"
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()
    def_str_(self):
        return f"{self.code} - {self.discount_percentage}%"