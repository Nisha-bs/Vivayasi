from .serializers import EmployeeSerializer, FarmerSerializer
from .models import Employee, Farmer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def create_employee(request):
    if request.method=='GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(data=employees, many=True)
        if serializer.is_valid():
            pass

        return Response(serializer.data)
    if request.method=='POST':
        serializer = EmployeeSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.error_messages)    

        return Response(serializer.data)

@api_view(['GET','POST'])
def create_farmer(request):
    if request.method =='GET':
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(data=farmers, many=True)
        if serializer.is_valid():
            pass

        return Response(serializer.data)
    if request.method=='POST':
        serializer = FarmerSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.error_messages)    

        return Response(serializer.data)
    