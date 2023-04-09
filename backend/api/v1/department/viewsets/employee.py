from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers import EmployeeSerializer
from ..utils import EmployeePagination
from backend.department.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = EmployeePagination

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('department__id', 'last_name',)

    def get_queryset(self, department_pk=None):
        _default_query = Employee.objects.select_related('department')

        if department_pk := self.kwargs.get('department_pk'):
            return _default_query.filter(department__pk=department_pk)

        return _default_query.all()
