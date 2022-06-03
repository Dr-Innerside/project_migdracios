from django import forms #장고 forms라는 클래스를 상속해줄거임
from .models import *

#2번
#forms에서는 모델 이름을 지정하고 모델의 항목들 중에서 어떤 field를 폼으로 보낼것인지 지정해줘야함.
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'avatar']