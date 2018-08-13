from django.contrib import admin
from django.urls import path

from .views import CondaRepodataAPIView, PackageAPIView, initialize

urlpatterns = [
    path('simple/', initialize),
    path('simple/<slug:pkg_name>/', PackageAPIView.as_view()),
    path('conda/<slug:arch>/repodata.json', CondaRepodataAPIView.as_view()),
]
