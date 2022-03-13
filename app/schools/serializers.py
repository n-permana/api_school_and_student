import uuid

from common.utils import time_stamp_hex_generator
from rest_framework import serializers

from schools import models


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = ["id", "name", "max_student"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ["id", "student_id", "firstname", "lastname", "school"]
        read_only_fields = ["student_id"]

    def school_is_full(self, target_school):
        students = models.Student.objects.filter(school=target_school).count()
        if students >= target_school.max_student:
            return True
        return False

    def create(self, validated_data):
        if self.school_is_full(validated_data["school"]):
            raise serializers.ValidationError(
                {"school": ["The school is already full"]}
            )

        student = models.Student(
            firstname=validated_data["firstname"],
            lastname=validated_data["lastname"],
            school=validated_data["school"],
        )
        student.student_id = time_stamp_hex_generator()
        student.save()
        return student
