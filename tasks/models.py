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
    task_pay = models.FloatField(null=True, blank=True)

    def __str__(self):
        self.task_pay = (self.task_rate)*(self.hours)
        super(Task, self).save()
        return self.title


