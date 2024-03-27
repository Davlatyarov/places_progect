from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)











class RegisterView(View):
    def get(self, request):
        
        form = RegisterForm
        
        
        return render(request, 'users/register.html', context={'form': form})
    
    
    def post(self, request):
        
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('landing_page')
        
        return render(request, 'users/register.html', context={'form': form})
    
    
class LoginView(View):
    def get(self, request): 
        form = LoginForm()
        
        return render(request, 'users/login.html', context={'form': form})
    
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('landing_page')
        
        return render(request, 'users/login.html', context={'form': form})  
    
    
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, 'users/profile.html', context={'form': form})
    
    def post(self, request):
        profile_update_form  = ProfileUpdateForm(instance=request.user, data=request.POST)
        
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('landing_page')
        
        return render(request, 'users/profile.html', context={'form': profile_update_form})
    
    
class ProfileView(View):
    def get(self, request):
        
        return render(request, 'users/profile_new.html')