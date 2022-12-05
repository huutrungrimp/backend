from .models import Task
from accounts.serializers import UserSerializer
from customers.serializers import CustomerSerializer
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'user', 'customer', 'title', 'date_time_start', 'date_time_end', 'hours']
