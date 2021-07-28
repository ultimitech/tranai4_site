# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.success(request, ("There was an error..."))
#             return redirect('login')
#     else:
#         return render(request, 'authenticate/login.html')

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):#RegisterUserView
  form_class = UserCreationForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')