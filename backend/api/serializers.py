from rest_framework import serializers

from .models import JobApplication

class JobApplicationSerialier(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')