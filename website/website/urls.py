from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from accounts import views as acc_view

acc_router = DefaultRouter()

acc_router.register('register', acc_view.ProfileRegisterAPIView)

posts_router = DefaultRouter()


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),
    path('api/accounts/', include(acc_router.urls)),
]