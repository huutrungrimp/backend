from django.db import models
from customers.models import Customer
from accounts.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    title = models.TextField(null=True)
    date_time_start = models.DateTimeField()
    date_time_end = models.DateTimeField()
    hours = models.FloatField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    task_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

    def task_pay(self):
        amount = self.hours*self.task_pay
        return amount

