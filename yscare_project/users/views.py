from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from yscare.models import GlucoseData, SleepData, StepData, HeartrateData
from datetime import datetime

User = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:main')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

@login_required
def main_view(request):
    user = request.user

    sleep = SleepData.objects.filter(user=user).last()
    steps = StepData.objects.filter(user=user).last()
    glucose = GlucoseData.objects.filter(user=user).last()
    heart = HeartrateData.objects.filter(user=user).last()

    context = {
        'name': user.name,
        'gender': '남성' if user.gender == 0 else '여성',
        'age': user.age,
        'sleep_duration': sleep.sleep_duration_minutes if sleep else None,
        'step_count': steps.step_count if steps else None,
        'glucose_level': glucose.glucose_level if glucose else None,
        'bpm': heart.bpm if heart else None,
    }

    return render(request, 'main.html', context)

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use.')
            return render(request, 'signup.html')

        user = User(
            username=username,
            name=name,
            email=email
        )
        user.set_password(password1)
        user.save()
        return redirect('users:health_info')

    return render(request, 'signup.html')

@login_required
def health_info_view(request):
    user = request.user

    if request.method == 'POST':
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password1 != password2:
            return render(request, 'health_info.html', {
                'error': '비밀번호가 일치하지 않습니다.',
                'username': user.username,
                'height': height,
                'weight': weight,
                'gender': gender,
                'age': age,
            })

        user.height = float(height) if height else None
        user.weight = float(weight) if weight else None
        user.gender = int(gender) if gender is not None else None
        user.age = int(age) if age else None

        if password1:
            user.set_password(password1)

        user.save()
        return redirect('users:main')

    context = {
        'username': user.username,
        'height': user.height,
        'weight': user.weight,
        'gender': user.gender,
        'age': user.age,
    }

    return render(request, 'health_info.html', context)
