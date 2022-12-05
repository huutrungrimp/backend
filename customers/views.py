from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Customer
from .serializers import CustomerSerializer
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework import status




@api_view(['GET','PUT'])
def updateCustomer(request, username, id):
    try:
        customer = Customer.objects.get(id=id, user=User.objects.get(username=username)) 
        
    except Customer.DoesNotExist:
        return Response({"error": "The customer is not found"}, status=404)

    if request.method == "GET":
        serializer = CustomerSerializer(customer, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        request.data._mutable = True # New
        if len(request.data['phone']) == 0: # Check if phone input is empty before using replace
            request.data['phone'] = None # assign the field is empty
            return Response(request.data)
        else:
            updatePhone = int(request.data['phone'].replace("'", "").replace('"', '')) # Help to remove "" or '' when string passed in
            request.data['phone'] == updatePhone
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'message': 'You do not have permision.'})



@api_view(['DELETE'])
def deleteCustomer(request, username, id):
    customer = Customer.objects.get(id=id, user = User.objects.get(username=username))
    customer.delete()

    return Response({'message': 'Post was deleted'})



@api_view(['GET'])
def customerDetail(request, username, id):
    customer = Customer.objects.get(id=id, user=User.objects.get(username=username))
    serializers = CustomerSerializer(customer, many=False)

    return Response(serializers.data)



@api_view(['GET'])
def customerList(request, username):
    customers = Customer.objects.all()
    serializers = CustomerSerializer(customers, many=True)

    return Response(serializers.data)



@api_view(['POST'])
def addCustomer(request, username):

    if request.method != "POST":
            return Response({"error": "POST request required."})

    customerName = request.data["customerName"]
    email = request.data["email"]
    phone = request.data["phone"]
    address = request.data["address"]
    city = request.data["city"]
    province = request.data["province"]
    postal = request.data["postal"]
    country = request.data["country"]

    try:
        
        user = User.objects.get(username=username)
        customer = Customer.objects.create(
            user = user, 
            customerName = customerName, 
            email = email, 
            phone = None, 
            address = address, 
            city = city, 
            province = province, 
            postal = postal, 
            country = country
        )

        if len(phone) == 0:
            customer.save()        
            return Response(CustomerSerializer(customer).data)
        else:
            phone = int(request.data['phone'].replace("'", "").replace('"', '')) # Help to remove "" or '' when string passed in
            customer.phone = phone
            customer.save()        
            return Response(CustomerSerializer(customer).data)
 
    except IntegrityError:
        return Response({"message": "something wrong"})

