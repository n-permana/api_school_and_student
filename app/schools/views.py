from dataclasses import fields

from django.shortcuts import render
from rest_framework import viewsets

from schools import models, serializers


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.SchoolSerializer

    def get_queryset(self):
        queryset = models.School.objects.all()
        fields = ["name", "max_student"]
        for field in fields:
            param = self.request.query_params.get(field)
            if param:
                lookup = "%s__contains" % field
                queryset = queryset.filter(**{lookup: param})
        ordering = self.request.query_params.get("ordering")
        if ordering and ordering.replace("-", "") in fields:
            queryset = queryset.order_by(ordering)
        return queryset


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        queryset = models.Student.objects.all()
        fields = ["firstname", "lastname", "student_id"]
        for field in fields:
            param = self.request.query_params.get(field)
            if param:
                lookup = "%s__contains" % field
                queryset = queryset.filter(**{lookup: param})
        school = self.request.query_params.get("school")
        if school:
            queryset = queryset.filter(school__name__icontains=school)
        ordering = self.request.query_params.get("ordering")
        if ordering and ordering.replace("-", "") in fields:
            queryset = queryset.order_by(ordering)
        return queryset


class SchoolStudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = models.Student.objects.filter(school=self.kwargs["schools_pk"])
        fields = ["firstname", "lastname", "student_id"]
        for field in fields:
            param = self.request.query_params.get(field)
            if param:
                lookup = "%s__contains" % field
                queryset = queryset.filter(**{lookup: param})
        school = self.request.query_params.get("school")
        if school:
            queryset = queryset.filter(school__name__icontains=school)
        ordering = self.request.query_params.get("ordering")
        if ordering and ordering.replace("-", "") in fields:
            queryset = queryset.order_by(ordering)
        return queryset

    serializer_class = serializers.StudentSerializer
