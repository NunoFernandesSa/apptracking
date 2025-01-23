from django.db import models


class JobApplication(models.Model):
    job = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    job_link = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)