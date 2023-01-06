from .serializers import EmployeeSerializer
from .models import Employee
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
        print(request.data)
        serializer = EmployeeSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.error_messages)    

        return Response(serializer.data)