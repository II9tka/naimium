from rest_framework import viewsets

from ..serializers import DepartmentSerializer
from backend.department.models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.all()
