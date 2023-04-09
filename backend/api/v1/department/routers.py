from backend.utils.routers import lazy_router, lazy_nested_router
from .viewsets import view_sets_, EmployeeViewSet

router = lazy_router(view_sets_)
department_router = lazy_nested_router('departments', EmployeeViewSet, router)
