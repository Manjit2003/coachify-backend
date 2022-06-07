from rest_framework import serializers

from coachify.users.models import Class, Parent, Student, Teacher


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    parent = ParentSerializer(
        read_only=True,
    )

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("id",)


class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"


class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ["name", "description", "teacher", "students"]
