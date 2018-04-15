"""policyinsights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from django.contrib.flatpages import views as flatpage_views
from django.urls import path, include
from django.views.generic import TemplateView

from locations.views import LocationsList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LocationsList.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('', include('profiles.urls')),
    path('', include('locations.urls')),
    path('', include('programs.urls')),
    path('', include('tags.urls')),
    path('', include('feedback.urls')),
    path('about/', flatpage_views.flatpage, {'url': '/about/'}, name='about'),
    path('accounts/', include('registration.backends.default.urls')),
    path('comments/', include('django_comments.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('terms-of-use', TemplateView.as_view(template_name='terms-of-use.html'), name='terms-of-use'),
    path('privacy-policy', TemplateView.as_view(template_name='privacy-policy.html'), name='privacy-policy'),
]
