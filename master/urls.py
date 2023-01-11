from django.contrib import admin
from django.urls import path, include
from authentication.views import UserApiRegister
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
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", include(router.urls)),
    path("", include(router_project.urls)),
    path("", include(router_issue.urls)),
]
