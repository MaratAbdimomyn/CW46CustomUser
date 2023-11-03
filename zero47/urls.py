from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dashboard.as_view(), name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', UserList.as_view(), name='home'),
    path('about/<int:pk>', AboutUser.as_view(), name='about'),
    path('login/', Login.as_view(), name='login'),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    path('positive/', Positive.as_view(), name='positive'),
    path('negative/', Negative.as_view(), name='negative'),
]
