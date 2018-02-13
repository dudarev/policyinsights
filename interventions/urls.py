from django.urls import path
from interventions import views as intervention_views


urlpatterns = [
    path('locations/search', intervention_views.LocationsSearchView.as_view(), name='location-search'),
    path('locations/<int:pk>', intervention_views.LocationDetail.as_view(), name='location-detail'),
    path(
        'locations/<int:location_pk>/intervention-categories/search',
        intervention_views.InterventionCategoriesSearchView.as_view(), name='intervention-category-search'),
    path(
        'intervention-categories/<int:intervention_category_pk>',
        intervention_views.InteventionsSearchView.as_view(), name='intervention-search'),
]
