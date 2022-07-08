from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import (
    EnrollStatus,
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
        skills = request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills) # ["mysql","python"]

        # job_skills = JobPostSkillSet.objects.filter(
        #     Q(skill_set__name='python') | Q(skill_set__name='mysql')
        # )

        query = Q()  # Q(skill_set__name='python') | Q(skill_set__name='mysql') | Q
        for skill in skills:
            query.add(Q(skill_set__name=skill), Q.OR)

        job_skills = JobPostSkillSet.objects.filter(query)

        job_posts = JobPost.objects.filter(
            id__in=[job_skill.job_post.id for job_skill in job_skills]
        )

        if job_posts.exists():
            serializer = JobPostSerializer(job_posts, many=True)
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)


class JobView(APIView):

    def post(self, request):
        job_type = int(request.data.get("job_type", None))
        # job_type = request.data.get("job_type", None)
        company_name = request.data.get("company_name", None)

        # 직업 유형 처리
        job_type_qs = JobType.objects.filter(id=job_type)
        # job_type_qs = JobType.objects.filter(job_type=job_type)
        if not job_type_qs.exists():
            return Response({"message": "invalid job type"}, status=status.HTTP_400_BAD_REQUEST)

        # 회사 이름 처리
        company = Company.objects.filter(company_name=company_name)
        if not company.exists():
            company = Company(company_name=company_name).save()
        else:
            company = company.first()

        # request.data.pop('job_type', None)
        job_serializer = JobPostSerializer(data=request.data)
        if job_serializer.is_valid():
            job_serializer.save(company=company, job_type=job_type_qs.first())
            return Response(status=status.HTTP_200_OK)

        return Response(job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    

from .serializers import EnrollStatusSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class StatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
        
    def get(self, request):
        enroll_status = EnrollStatus.objects.all()
        enroll_status = {
            "worker" : enroll_status.worker,
            "job_post" : enroll_status.job_post    
        }
        
        print(f"enroll_status->{enroll_status}")
        return Response()
    
    def post(self, request):
        request.data['worker'] = request.user
        request.data['job_post'] = JobPost.objects.get(id=request.data['job_post'])
        serializer = EnrollStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"message":"지원에 성공했습니다."})