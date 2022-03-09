from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # templates
    path('record-app/', include('record_app.urls')),
    # apis
    path('api/v1/record-app/', include('record_app.urls_api')),

    path('admin/', admin.site.urls),
]
