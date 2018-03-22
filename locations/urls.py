from django.urls import path, re_path

from locations import views


urlpatterns = [
    path('l/', views.LocationCreate.as_view(), name='location-create'),
    re_path(r'^l/(?P<slug>[-%\w]+)/$', views.LocationDetail.as_view(), name='location-detail'),
    re_path(r'^l/(?P<slug>[-%\w]+)/update/$', views.LocationUpdate.as_view(), name='location-update'),
    path('l/compare/<int:pk>/', views.LocationCompareSelect.as_view(), name='location-compare-select'),
    path('l/compare/<int:pk1>/<int:pk2>/', views.LocationsCompare.as_view(), name='location-compare'),
]
