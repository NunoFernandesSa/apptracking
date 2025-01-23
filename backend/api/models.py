from django.db import models


class JobApplication(models.Model):
    job = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    job_link = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job + ' at ' + self.company_name}"
