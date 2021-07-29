# from django.urls import path
# from .views import UserRegisterView

# urlpatterns = [
#     path('register/', UserRegisterView.as_view(), name='register'),
# ]


from django.urls import path
from . import views

urlpatterns = [path('signup/', views.SignUp.as_view(), name='signup'), ]