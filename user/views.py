from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import auth
from .models import UserModel
import re

# Create your views here.
def intro(request):
    if request.method == 'GET':
        return render(request, 'intro.html')


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if email == '' or username == '' or password == '':
            return render(request, 'user/signup.html', {'error': '빈 칸에 내용을 입력해 주세요!'})
        else:
            if not(6 < len(password) < 21):
                return render(request, 'user/signin.html', {'error': 'password 길이는 7~20자 입니다.'})
            elif re.search('[0-9]+', password) is None or re.search('[a-zA-Z]+', password) is None:
                return render(request, 'user/signin.html', {'error': 'password 형식은 영문,숫자 포함 7~20자 입니다.'})
            elif password != password2:
                return render(request, 'user/signup.html', {'error': 'password 확인 해 주세요!'})
            if re.search('[0-9]+', username) is None or re.search('[a-zA-Z]+', username) is None:
                return render(request, 'user/signin.html', {'error': 'ID에 영문,숫자는 필수입니다.'})

            exist_user = get_user_model().objects.filter(username=username)
            exist_email = get_user_model().objects.filter(email=email)

            if exist_email:
                return render(request, 'user/signin.html', {'error': '이미 사용 중인 email입니다.'})
            elif exist_user:
                return render(request, 'user/signin.html', {'error': '이미 사용 중인 ID입니다.'})
            else:
                UserModel.objects.create_user(email=email, username=username, password=password, bio=bio)
                return redirect('/sign-in')



def sign_in_view(request):
    # 회원가입 로그인 화면이 같은 HTML임으로
    # if request.method == 'GET':
    #     user = request.user.is_authenticated
    #     if user:
    #         return redirect('/')
    #     else:
    #         return render(request, 'user/signin.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        true_user = auth.authenticate(request, username=username, password=password)
        if true_user is not None:
            auth.login(request, true_user)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': ' ID 또는 패스워드를 확인해주세요!'})



@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')