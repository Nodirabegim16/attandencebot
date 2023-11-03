from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Group, Attendance, Student
from .serializers import GroupSerializer, AttendanceSerializer, StudentSerializer


class GroupList(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

class StudentView(APIView):
    def get(self, request, group_id):
        students = Student.objects.filter(group_id=group_id)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


