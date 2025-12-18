from django.db import models
from django.contrib.auth.models import User
from MessagesTemplates.models import MessageTemplate
# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    fee = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    def __str__(self):
        return self.name
    

class ScheduleBulkMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    templates = models.ForeignKey(MessageTemplate, on_delete=models.CASCADE)
    customers = models.ManyToManyField(Customer)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)