from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Employees(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

    def get(self, request, id=None, format=None):
        if id:
            emp = Employee.objects.get(id=id)
            data = {}
            data = {
                'id':emp.id,
                'name': emp.firstname + ' '+ emp.lastname,
                'emp_code': emp.emp_code,
                'email': emp.email,
                'address': {'lan1':emp.lan1,'lan2':emp.lan2,'dist':emp.dist,'state':emp.state,'country':emp.country},
                'blood_group': emp.blood_group,
                'phone_no': emp.phone_no,
                'designation': emp.designation,
                'marital_status': emp.marital_status,
                'department': emp.department,
                'grade_level': emp.grade_level
            }
            return Response(data, status=status.HTTP_200_OK)
        employees = Employee.objects.all()
        data = {}
        lst = []
        for emp in employees:
            data = {
                'id':emp.id,
                'name': emp.firstname + ' '+ emp.lastname,
                'emp_code': emp.emp_code,
                'email': emp.email,
                'address': {'lan1':emp.lan1,'lan2':emp.lan2,'dist':emp.dist,'state':emp.state,'country':emp.country},
                'blood_group': emp.blood_group,
                'phone_no': emp.phone_no,
                'designation': emp.designation,
                'marital_status': emp.marital_status,
                'department': emp.department,
                'grade_level': emp.grade_level
            }
            lst.append(data)
        return Response(lst, status=status.HTTP_200_OK)
    
    # def get(self, request, id=None, format=None):
    #     try:
    #         if id:
    #             emp = Employee.objects.get(id=id)
    #             serializer = EmployeeSerializer(emp)
    #             return Response(serializer.data)
            
    #         emp = Employee.objects.all()
    #         serializer = EmployeeSerializer(emp, many=True)

    #         return Response(serializer.data)
    #     except Exception as e:
    #         print(e)

    # def put(self, request, id, format=None):
    #     try:
    #         emp = Employee.objects.get(id=id)
    #         req = request.data
    #         if emp.emp_code == req['emp_code'] or emp.email == req['email']:
    #             return Response('do not update')
            
    #         serializer = EmployeeSerializer(emp, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #     except Exception as e:
    #         print(e)

    def put(self, request, id, format=None):
        try:
            emp = Employee.objects.get(id=id)
            req = request.data
            if emp.emp_code == req.get('emp_code') or emp.email == req.get('email'):
                return Response('Do not update emp_code or email')
            serializer = EmployeeSerializer(emp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            print(e)


    def delete(self, request, id, format=None):
        try:
            emp = Employee.objects.filter(id=id)
            emp.delete()
            return Response('successfully delete',status=status.HTTP_204_NO_CONTENT)    
        except Exception as e:
            print(e)



class EmployeeSearch(ListAPIView):       
    queryset = Employee.objects.all()
    serializer_class  = EmployeeSerializer    
    filter_backends = [SearchFilter]
    search_fields = ["department", "grade_level", 'designation', 'marital_status', 'firstname', 'lastname']

