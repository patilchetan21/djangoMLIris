from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('basiConcepts.urls')),
    path("", include('irisApp.urls')),
    path("admin/", admin.site.urls),
]
