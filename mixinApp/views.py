from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    ListModelMixin
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    viewsets.ModelViewSet: handles all pk and non-pk based operations
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentList(ListCreateAPIView):
#     """
#     Non-pk based operations
#     ListCreateAPIView: handles listing all model objects and creating a new student object
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetail(RetrieveUpdateDestroyAPIView):
#     """
#     PK-based operations
#     RetrieveUpdateDestroyAPIView: handles get(single), put(update), and delete(destroy) request
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     """
#     Non-primary based endpoints
#     ListModelMixin: retrieves all Student objects in the DB
#     CreateModelMixin: creates a new object
#     GenericAPIView: Base class for all other generic views
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request):
#         """ gets all the student objects using ListModelMixin"""
#         return self.list(request)
#
#     def post(self, request):
#         """ inherits from CreateModelMixin: used to create a new Student object """
#         return self.create(request)
#
#
# class StudentDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     """
#     RetrieveModelMixin: gets a single student
#     UpdateModelMixin: for updating a single object
#     DestroyModelMixin: handles delete request
#     GenericAPIView: Base class for all other generic views.
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, pk):
#         """
#         pk: retrieves a single record
#         """
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
