from django.urls import path, include

urlpatterns = [
    path('', include('backend.api.v1.department.urls')),
]
