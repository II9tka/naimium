from rest_framework import serializers

from backend.department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    total_employees = serializers.IntegerField(read_only=True)
    total_salary_employees = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'
