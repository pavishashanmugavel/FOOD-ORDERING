from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, default="Unknown Address")
    item_name = models.CharField(max_length=100, default="Unknown Item")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.item_name} ({self.quantity})"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name