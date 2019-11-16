"""aaaimxadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from productivity.views import *
from finances.views import MembershipViewSet

admin.site.site_header = "AAAIMX Admin"
admin.site.site_title = "AAAIMX Admin Portal"
admin.site.index_title = "Welcome to AAAIMX Administration Portal"


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'members', MemberViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'divisions', DivisionViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'lines', LineViewSet)
router.register(r'research', ResearchViewSet)
router.register(r'thesis', ThesisViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'presentations', PresentationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('jet/', include('jet.urls', namespace='jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)