from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class ProjectMetadata(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    local_csv_file_location = models.CharField(max_length=255)
    s3_model_location = models.CharField(max_length=255)
    model_evaluation_results = models.TextField()

