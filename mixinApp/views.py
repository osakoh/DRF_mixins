from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    ListModelMixin
from .models import Student
from .serializers import StudentSerializer


class StudentList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Non-primary based endpoints
    ListModelMixin: retrieves all Student objects in the DB
    CreateModelMixin: creates a new object
    GenericAPIView: Base class for all other generic views.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        """ gets all the student objects using ListModelMixin"""
        return self.list(request)

    def post(self, request):
        """ inherits from CreateModelMixin: used to create a new Student object """
        return self.create(request)
