from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dadosQuiz.views import home
from quiz.views import GerarQuestaoAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('quiz/', include('quiz.urls')),
]
