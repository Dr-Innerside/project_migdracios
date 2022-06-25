from rest_framework import serializers

from .models import (
    SkillSet as SkillSetModel , 
    JobPostSkillSet as JobPostSkillSetModel ,
    JobPost as JobPostModel ,
    JobType as JobTypeModel ,
    Company as CompanyModel ,
    CompanyBusinessArea as CompanyBusinessAreaModel , 
    BusinessArea as BusinessAreaModel ,
)

# 1번. Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["id", "company_name"]

# 3번. JobType Serializer
class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = ["id", "job_type"]

# 2번. JobPost Serializer
class JobPostSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    skillsets = serializers.SerializerMethodField()
    position_type = serializers.SerializerMethodField()
    def get_skillsets(self, obj):
        print(f"obj->{obj.jobpostskillset_set.all()}")
        return [i.skill_set.name for i in obj.jobpostskillset_set.all()]
    
    def get_position_type(self, obj):
        return obj.job_type.job_type

    class Meta:
        model = JobPostModel
        fields = [
            "id", "position_type", "company", "job_description", "salary", "skillsets"
        ]

        extra_kwargs = {
            'job_type': {
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.'
                },
                # required : validator에서 해당 값의 필요 여부를 판단한다.
                'required': False  # default : True
            },
        }