from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('', views.StudentList.as_view()),
    # path('<int:pk>/', views.StudentDetail.as_view()),
]
