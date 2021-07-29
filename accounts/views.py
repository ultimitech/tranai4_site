from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# class UserRegisterView(generic.CreateView):#RegisterUserView
#   form_class = UserCreationForm
#   success_url = reverse_lazy('login')
#   template_name = 'registration/register.html'

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'