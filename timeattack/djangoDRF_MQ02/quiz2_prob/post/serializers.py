from rest_framework import serializers

from .models import Company as CompanyModel
from .models import JobPost as JobPostModel
from .models import JobPostSkillSet as JobPostSkillSetModel


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyModel
        fields = "__all__"

class JobPostSerializer(serializers.ModelSerializer):
    


    class Meta:
        model = JobPostModel
        fields = "__all__"

class JobPostSkillSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostSkillSetModel
        fields = "__all__"
