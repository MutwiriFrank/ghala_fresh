
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(
    title="Ghala Foods",
    default_version='v1',
    description="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4OTU2Mjg2LCJpYXQiOjE2NTgzNTYyODYsImp0aSI6ImM3MGJhNGJlZDY4ODQxNTQ4MzA4OTFhY2Q5OGQ0ZTQyIiwidXNlcl9pZCI6Mn0.bgGYjFTRuMvAMZYCsqeakFWGcBAJ1U9gzpd4f-ndz44",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [

    path('admin', admin.site.urls),
    
    # users
    path('users/', include('users.urls', namespace='users' )),

    # django rest web login
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),

    # documentation
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

