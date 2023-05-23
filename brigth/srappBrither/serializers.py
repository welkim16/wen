from rest_framework import serializers
from .models import Jobs,JobDetail



class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobDetail
        fields='__all__'
class JobSerializer(serializers.ModelSerializer):
    job_details=JobDetailSerializer(many=True,read_only=True,source='job_details')
    class Meta:
        model=Jobs
        fields=['id','title','link','job']