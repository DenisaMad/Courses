"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from StudentiApp.views import Test , Test2, salveaza_user
from ProfesoriApp.views import salveaza_profesor
from AnUnivApp.views import an_universitar

schema_view = get_schema_view(
    openapi.Info(
        title="InterviewCrusher",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('api/Test', Test, name="Test"),
    path('api/Test2', Test2, name="Test2"),
    path('api/save_user', salveaza_user, name="salveaza user"),
    path('api/prof', salveaza_profesor, name="salveaza profesor"),
    path('api/an_universitar', an_universitar, name="salveaza an"),

]

