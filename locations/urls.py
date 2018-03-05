from django.urls import path

from locations import views


urlpatterns = [
    path('l/', views.LocationCreate.as_view(), name='location-create'),
    path('l/<slug:slug>/', views.LocationDetail.as_view(), name='location-detail'),
    path('l/<slug:slug>/update/', views.LocationUpdate.as_view(), name='location-update'),
    path('l/compare/<int:pk>/', views.compare_select, name='location-compare-select'),
    path('l/compare/<int:pk1>/<int:pk2>/', views.compare, name='location-compare'),
]
