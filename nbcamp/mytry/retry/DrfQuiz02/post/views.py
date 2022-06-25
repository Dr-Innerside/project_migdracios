from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet as JobPostSkillSetModel,
    JobType as JobTypeModel,
    JobPost as JobPostModel,
    Company as CompanyModel,
)
from django.db.models.query_utils import Q

from .serializers import (
    CompanySerializer,
    JobPostSerializer,
    )


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def get(self, request):
        '''
        POST맨으로 GET 요청한 JSON 데이터를 시리얼라이저로 보내기
        company_name은 그냥 문자열이고, 오브젝트 형으로 변환해서 보내야 요목조목 뜯어서
        데이터를 필드에 맞게 정제해 리턴해 줄 수 있다.
        '''

        # CompanySerializer Test

        # ===
        # request_comp = request.data.get("company_name")
        # target_comp = CompanyModel.objects.get(company_name=request_comp)
        # print(f"request_comp->{request_comp}")
        # print(f"target_comp->{target_comp}")
        # return Response(CompanySerializer(target_comp).data)
        # ===

        
        # JobPostSerializer Test

        # ===
        request_jobpost_num = request.data.get("jobpost")
        target_jobpost = JobPostModel.objects.get(id=request_jobpost_num)
        print(f"request_jobpost_num->{request_jobpost_num}")
        print(f"target_jobpost->{target_jobpost}")
        print(f"dir target_jobpost ->{dir(target_jobpost)}")
        return Response(JobPostSerializer(target_jobpost).data)
        # ===

    def post(self, request):
        job_type = int( request.data.get("job_type", None) )
        company_name = request.data.get("company_name", None)

        return Response(status=status.HTTP_200_OK)

