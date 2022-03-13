from django.shortcuts import render
from rest_framework import viewsets

from schools import models, serializers


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class SchoolStudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return models.Student.objects.filter(school=self.kwargs["schools_pk"])

    serializer_class = serializers.StudentSerializer
