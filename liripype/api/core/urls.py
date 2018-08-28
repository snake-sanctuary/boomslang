from django.contrib import admin
from django.urls import path

from .views import (
    CondaRepodataAPIView, PackageAPIView, initialize, DownloadBuildAPIView,
    UploadPypiAPIView,
)

urlpatterns = [
    path('simple/', initialize),
    path('simple/<slug:pkg_name>/', PackageAPIView.as_view()),
    path('conda/<slug:arch>/repodata.json', CondaRepodataAPIView.as_view()),
    path('download/build/<int:pk>/<filename>/', DownloadBuildAPIView.as_view(), name="download-build"),
    path('pypi/api/', UploadPypiAPIView.as_view()),
    #path('conda/<slug:arch>/repodata.json', CondaRepodataAPIView.as_view()),
]
