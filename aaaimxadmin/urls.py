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
from django.views.generic.base import TemplateView

# REST FRAMEWORK
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from .views import UserViewSet, GroupViewSet
from storage.views import *
from productivity.views import *
from finances.views import *
from logistic.views import *

# SIMPLE JTW
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .token import MyTokenObtainPairView

admin.site.site_header = "AAAIMX Admin"
admin.site.site_title = "AAAIMX Admin Portal"
admin.site.index_title = "Welcome to AAAIMX Administration Portal"
admin.site.site_url = "http://www.aaaimx.org"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter() # routers.SimpleRouter(trailing_slash=False)
router.register(r"users", UserViewSet)
router.register(r"roles", RoleViewSet)
router.register(r"members", MemberViewSet)
router.register(r"advisors", AdvisorViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"partners", PartnerViewSet)
router.register(r"memberships", MembershipViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"events", EventViewSet)
router.register(r"divisions", DivisionViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"lines", LineViewSet)
router.register(r"research", ResearchViewSet)
router.register(r"invoices", InvoiceViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

api_urlpatterns = [
    path("", include(router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('accounts/', include('rest_registration.api.urls')),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("storage/", ftp_list)
]

urlpatterns = [

    # APPLICATION
    path("", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    path("image/", image),
    path("membership/", membership),

    # DOCS
    path('openapi', get_schema_view(
        title="AAAIMX API",
        description="API for productivity …",
        version="1.1.0"
    ), name='openapi-schema'),
    path('docs', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
