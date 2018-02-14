from django.urls import path
from interventions import views


urlpatterns = [
    path('locations/search', views.LocationsSearchView.as_view(), name='location-search'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='location-detail'),
    path(
        'locations/<int:location_pk>/intervention-categories/search',
        views.InterventionCategoriesSearchView.as_view(), name='intervention-category-search'),
    path(
        'intervention-categories/<int:intervention_category_pk>',
        views.InterventionsSearchView.as_view(), name='intervention-search'),
    path(
        'interventions/<int:pk>',
        views.InterventionsDetailView.as_view(), name='intervention-detail'),
]
