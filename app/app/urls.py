"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path

# from rest_framework import routers
from rest_framework_nested import routers
from schools import views

# School Router
school_router = routers.SimpleRouter()
school_router.register(r"schools", views.SchoolViewSet)
nested_school_router = routers.NestedSimpleRouter(
    school_router, r"schools", lookup="schools"
)
nested_school_router.register(
    r"students", views.SchoolStudentViewSet, basename="school-student"
)
# Student Router
student_router = routers.SimpleRouter()
student_router.register(r"students", views.StudentViewSet)

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include(school_router.urls)),
    path("", include(nested_school_router.urls)),
    path("", include(student_router.urls)),
]
