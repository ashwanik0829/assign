# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import Tenant, ProjectMetadata

@csrf_exempt
def save_project_metadata(request):
    try:
        if request.method == 'POST':
            tenant_id = request.POST.get('tenant_id')
            local_csv_file_location = request.POST.get('local_csv_file_location')
            s3_model_location = request.POST.get('s3_model_location')
            model_evaluation_results = request.POST.get('model_evaluation_results')

            project_metadata = ProjectMetadata.objects.create(
                tenant_id=tenant_id,
                local_csv_file_location=local_csv_file_location,
                s3_model_location=s3_model_location,
                model_evaluation_results=model_evaluation_results
            )

            return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
def get_tenant_and_project_metadata(request):
    try:
        if request.method == 'GET':
            tenant = Tenant.objects.latest('id')
            project_metadata = ProjectMetadata.objects.latest('id')

            response_data = {
                'tenant': {
                    'id': tenant.id,
                    'name': tenant.name,
                    'email': tenant.email
                },
                'project_metadata': {
                    'id': project_metadata.id,
                    'local_csv_file_location': project_metadata.local_csv_file_location,
                    's3_model_location': project_metadata.s3_model_location,
                    'model_evaluation_results': project_metadata.model_evaluation_results
                }
            }

            return JsonResponse(response_data)
    except ObjectDoesNotExist:
        return JsonResponse({'success': False, 'error': 'Records not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
