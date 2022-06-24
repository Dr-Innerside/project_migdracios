from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)

from .serializers import JobPostSerializer

from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        print("잡 포스트 접근")
        job_type_id = int(request.data.get("job_type", None) )
        company_name = request.data.get("company_name", None)
        job_description = request.data.get("job_description", None)
        salary = int(request.data.get("salary"))

        print(f"job_type_id-->{job_type_id}")
        print(f"company_name-->{company_name}")
        print(f"job_description-->{job_description}")
        print(f"salary-->{salary}")

        post_sources = {
            "job_type_id" : job_type_id,
            "company_name" : company_name,
            "job_description" : job_description,
            "salary" : salary
        }

        return Response(JobPostSerializer(post_sources).data, status=status.HTTP_200_OK)

