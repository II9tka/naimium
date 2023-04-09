from django.urls import path, include

from .routers import router, department_router

urlpatterns = [
    path('', include(router.urls)),
    path('', include(department_router.urls))
]
