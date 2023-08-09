"""
URL configuration for my_tna_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
import pendulum


def index(request):
    now = pendulum.now("Europe/London")
    data = ("<h1>Hello world</h1>"
            f"<p>The date is {now.to_iso8601_string()}")
    return HttpResponse(data)


def healthcheck(request):
    return HttpResponse("okay")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("healthcheck/live", healthcheck, name="healthcheck"),
]
