from rest_framework import viewsets

from coachify.users.api.serializers import (
    ClassSerializer,
    ParentSerializer,
    StudentSerializer,
    TeacherSerializer,
)
from coachify.users.models import Class, Parent, Student, Teacher


class TeacherAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ParentAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parents to be viewed or edited.
    """

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ClassAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows classes to be viewed or edited.
    """

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
