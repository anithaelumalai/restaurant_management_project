from django .db import models

class OrderStatus(models.Model):
    name = models.CharFIELD(max_length=50, unique=True)

    def__str__(self):
        return self.name


        class Order(models.Model):
            customer_name = models.CharField(max_length=100)
            total_price = models.DecimalField(max_digits=10,decimal_places=2)
            status = models.ForeignKey(orderStatus, on_delete=modeels.SET_NULL,null=True)

            def__str__(self):
                return f"order #{self.id} - {self.customer_name}"