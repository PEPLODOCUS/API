
from django.db import models

# Customer Model
class Customer(models.Model):
    # Defining customer fields
    name = models.CharField(max_length=100, help_text="The name of the customer.")
    email = models.EmailField(unique=True, help_text="The email of the customer.")

    def __str__(self):
        return self.name

    # You can add methods here if needed (e.g., to calculate loyalty points or something else)


# Order Model
class Order(models.Model):
    # Defining order fields
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, help_text="The date and time when the order was placed.")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount for the order.")

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

    class Meta:
        ordering = ['-order_date']  # Orders should be sorted by the latest order first.
