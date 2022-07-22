from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import User as UserModel
from post.models import (
    JobPost as JobPostModel,
    JobPostActivity as JobPostActivityModel,
    ApplyStatus as ApplyStatusModel,
    ) 

# Create your tests here.
class ApplyStatusTest(APITestCase):
    def setUp(self):
        '''
        테스트 코드 셋업
        1. 사용자 생성
        2. 잡포스트 생성
        3. 지원상태 생성
        4. 액티비티 생성
        5. 액세스 토큰 받기
        '''

        # 사용자 생성
        self.user_data = {"username":"david", "password":"1234", "email":"david@test.com"}
        self.user = UserModel.objects.create(**self.user_data)
        
        # # 잡포스트 생성
        self.job_post_data = {"job_description": "몰라", "salary": 20}
        self.jobpost = JobPostModel.objects.create("백엔드 엔지니어", 20)
        
        # # 지원상태 생성
        self.status_data = "submitted"
        self.status = ApplyStatusModel.objects.create(self.status_data)
        
        # # 액티비티 생성
        # self.activity = JobPostActivityModel.objects.create(self.status_data)
        
        # 토큰 받기
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
        
    def test_get_status(self):
        response = self.client.get(reverse("apply"))
        self.assertEqual(response.status_code, 200)
            
        