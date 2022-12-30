"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from authentication.views import UserApiLogin, UserApiRegister
from rest_framework_nested import routers

from globalapp.views import ProjectApiView, ContributorApiView, IssueApiView, CommentApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'signup', UserApiRegister)
router.register(r'projects', ProjectApiView)

router_project = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
router_project.register(r'users', ContributorApiView, basename='project_to_contributors')
router_project.register(r'issues', IssueApiView, basename='project_to_issue')

router_issue = routers.NestedSimpleRouter(router_project, r'issues', lookup='issues')
router_issue.register(r'comments', CommentApiView, basename='issue_to_comment')



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api_auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path("login/", UserApiLogin.as_view()),
    path("", include(router.urls)),
    path("", include(router_project.urls)),
    path("",include(router_issue.urls)),
]
