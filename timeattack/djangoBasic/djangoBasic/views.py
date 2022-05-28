import json
import hashlib
from django.http import HttpResponse
from django.shortcuts import render
from user.models import UserModel

def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        # print(f'email ->{email}, password->{password}')

        if '@' in email:

        else:
            
            return

        # pw_hash = hashlib.sha256(password)
        # pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        userdata = UserModel(email, password)
        userdata.email = email
        userdata.password = password

        # print(f'userdata -> {userdata}')
        # print(f'email-->{userdata.email}')
        # print(f'password-->{userdata.password}')

        return ''