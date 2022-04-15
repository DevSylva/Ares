from core.models import (
    Pupil,
    Teacher,
    Staff,
)
from rest_framework import serializers


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'sex',
            'passport',
            'phone_number',
            'email',
            'address',
            'parent_or_guardian_name',
            'parent_or_guardian_phone_numbers'
        )

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'sex',
            'passport',
            'phone_number',
            'email',
            'address',
            'parent_or_guardian_name',
            'parent_or_guardian_phone_numbers'
        )


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'sex',
            'passport',
            'role',
            'phone_number',
            'email',
            'address',
            'parent_or_guardian_name',
            'parent_or_guardian_phone_numbers'
        )
