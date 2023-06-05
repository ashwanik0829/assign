from django.urls import path
from .views import save_project_metadata, get_tenant_and_project_metadata

urlpatterns = [
    path('api/save-project-metadata/', save_project_metadata, name='save_project_metadata'),
    path('api/get-tenant-and-project-metadata/', get_tenant_and_project_metadata, name='get_tenant_and_project_metadata'),
]
